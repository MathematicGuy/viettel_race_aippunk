"""
Hybrid Collection Pipeline for RAG Multimodal Application

This module creates a complete hybrid search pipeline that processes markdown documents
with text and images, converts them to entities, and stores them in Milvus vector database.

Usage:
    ```python
    from core.hybrid_collection_pipeline import create_hybrid_pipeline
    from models.image_encoder import MultimodalImageEncoder
    from sentence_transformers import SentenceTransformer
    import clip

    # Initialize models
    text_model = SentenceTransformer('sentence-transformers/paraphrase-multilingual-mpnet-base-v2')
    clip_model, clip_preprocess = clip.load("ViT-B/32", device="cuda")
    image_encoder = MultimodalImageEncoder(clip_model, clip_preprocess)

    # Create pipeline
    process_docs, search_engine = create_hybrid_pipeline(
        markdown_dir="path/to/markdown",
        image_base_dir="path/to/images",
        uri="http://localhost:19530",
        token="root:Milvus",
        text_model=text_model,
        image_encoder=image_encoder
    )

    # Process documents
    markdown_files = [...]
    entities, search_engine = process_docs(markdown_files)
    ```
"""

import logging
from pathlib import Path
import sys
from typing import List, Tuple, Callable, Any

project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))
print('Core Path:', project_root)

from processors.markdown_processor import MarkdownProcessor
from processors.entity_processors import TextEntityProcessor, ImageEntityProcessor
from storage.milvus_store import MilvusStore
from retrieval.search_engine import HybridSearchEngine
from langchain_core.documents import Document

logger = logging.getLogger(__name__)


def create_hybrid_pipeline(markdown_dir: str, image_base_dir: str,
                            uri: str, token: str, text_model, image_encoder) -> Tuple[Callable, HybridSearchEngine]:
    """
    Create a complete hybrid search pipeline for processing markdown documents.

    This pipeline:
    1. Processes markdown files to extract text, tables, and images
    2. Converts content into text and image entities
    3. Stores entities as documents in Milvus vector database
    4. Returns a search engine for hybrid retrieval

    Args:
        markdown_dir: Directory containing markdown files
        image_base_dir: Base directory for storing/accessing images
        uri: Milvus URI (e.g., "http://localhost:19530")
        token: Milvus authentication token (e.g., "root:Milvus")
        text_model: Sentence transformer model for text embeddings
        image_encoder: Multimodal image encoder (CLIP-based)

    Returns:
        Tuple containing:
            - process_documents: Callable function to process markdown files
            - search_engine: HybridSearchEngine instance for retrieval

    Example:
        ```python
        process_docs, search_engine = create_hybrid_pipeline(
            markdown_dir="docs",
            image_base_dir="images",
            uri="http://localhost:19530",
            token="root:Milvus",
            text_model=text_model,
            image_encoder=image_encoder
        )

        markdown_files = list(Path("docs").glob("*.md"))
        entities, search_engine = process_docs(markdown_files)
        ```
    """

    logger.info(f"Creating hybrid pipeline for {markdown_dir}")

    # Initialize components
    processor = MarkdownProcessor(markdown_dir, image_base_dir)
    text_processor = TextEntityProcessor(text_model)
    image_processor = ImageEntityProcessor(image_encoder)

    # Initialize Milvus store
    store = MilvusStore(
        uri=uri,
        token=token,
        db_name="gil",
        # collection_name="multimodal_rag2",
        embed_model="sentence-transformers/paraphrase-multilingual-mpnet-base-v2",
        drop_old=True
    )

    # Initialize search engine
    search_engine = HybridSearchEngine(store.vector_store, text_model, image_encoder)

    logger.info("Pipeline components initialized successfully")

    def process_documents(markdown_files: List[Path]) -> Tuple[List[Document], HybridSearchEngine]:
        """
        Process markdown files into entities and store them in Milvus.

        This function:
        1. Extracts content from each markdown file
        2. Creates text and image entities
        3. Converts entities to LangChain Document objects
        4. Stores documents in Milvus vector database

        Args:
            markdown_files: List of Path objects pointing to markdown files

        Returns:
            Tuple containing:
                - all_documents: List of Document objects stored in Milvus
                - search_engine: HybridSearchEngine instance for retrieval
        """
        all_documents = []
        all_entities = []

        for md_file in markdown_files:
            print(f"\n{'='*60}")
            print(f"Processing: {md_file}")
            print(f"{'='*60}")

            try:
                # Extract content from markdown
                content = processor.extract_content(Path(md_file))
                print(f"  ✓ Text length: {len(content['text'])} characters")
                print(f"  ✓ Tables found: {len(content['tables'])}")
                print(f"  ✓ Images found: {len(content['images'])}")

                # Create text entities
                text_entities = text_processor.create_text_entities(content)
                print(f"  ✓ Text entities created: {len(text_entities)}")

                # Create image entities
                image_entities = image_processor.create_image_entities(content)
                print(f"  ✓ Image entities created: {len(image_entities)}")

                # Collect all entities
                all_entities.extend(text_entities)
                all_entities.extend(image_entities)

                logger.info(f"Processed {md_file}: {len(text_entities)} text + {len(image_entities)} image entities")

            except Exception as e:
                logger.error(f"Error processing {md_file}: {e}")
                print(f"  ✗ Error: {e}")
                continue

        # Convert entities to LangChain Documents and store in Milvus
        if all_entities:
            print(f"\n{'='*60}")
            print(f"Storing {len(all_entities)} entities to Milvus")
            print(f"{'='*60}")

            try:
                # Convert entities to Documents if needed
                documents = _convert_entities_to_documents(all_entities)

                # Add documents to vector store
                doc_ids = store.add_documents(documents)

                print(f"  ✓ Successfully stored {len(doc_ids)} documents in Milvus")
                logger.info(f"Added {len(doc_ids)} documents to Milvus collection")

                all_documents.extend(documents)

            except Exception as e:
                logger.error(f"Error storing entities to Milvus: {e}")
                print(f"  ✗ Error storing to Milvus: {e}")

        print(f"\n✅ Pipeline complete! Total {len(all_documents)} documents processed.")
        logger.info(f"Pipeline completed: {len(all_documents)} total documents")

        return all_documents, search_engine

    return process_documents, search_engine


def _convert_entities_to_documents(entities: List[Any]) -> List[Document]:
    """
    Convert entity objects to LangChain Document objects.

    Args:
        entities: List of entity objects (from text_processor and image_processor)

    Returns:
        List of LangChain Document objects with metadata
    """
    documents = []

    for entity in entities:
        try:
            # Handle entity as dict or object with attributes
            if isinstance(entity, dict):
                content = entity.get('content', '')
                metadata = entity.get('metadata', {})
            else:
                # Try to extract content from entity object
                content = getattr(entity, 'content', str(entity))
                metadata = getattr(entity, 'metadata', {})

            if content:
                # Ensure namespace field exists in metadata (required for partition_key_field)
                if 'namespace' not in metadata:
                    metadata['namespace'] = 'viettel'  # Add default namespace

                doc = Document(page_content=content, metadata=metadata)
                documents.append(doc)

        except Exception as e:
            logger.warning(f"Error converting entity to document: {e}")
            continue

    logger.info(f"Converted {len(documents)} entities to documents")
    return documents
