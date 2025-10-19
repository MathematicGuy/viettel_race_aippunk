import os
import shutil
import re
from pathlib import Path

import re
import subprocess
import os
# Run in parallel
from concurrent.futures import ThreadPoolExecutor, as_completed

#? Config MinerU
print('BEGIN PDF PREPROCESSING: COVERT PDF to MARKDOWN')
# PATH = "private-test-input/"
# OUTPUT_PATH = "private-test-output/"
PATH = 'Public_test_input'
OUTPUT_PATH = 'Public_test_output'


MAX_WORKERS = 3  # Adjust based on your VRAM and CPU

# ==== Device & Precision ====
os.environ["CUDA_VISIBLE_DEVICES"] = "0"
os.environ["MINERU_USE_GPU"] = "True"
os.environ["MINERU_DEVICE"] = "cuda"
os.environ["MINERU_USE_FP16"] = "True"
os.environ["MINERU_MAX_GPU_MEMORY"] = "16G"  # for your 16GB VRAM
os.environ["MINERU_ENABLE_PARALLEL"] = "true"  # process multiple pages at once

# ==== Batch & Memory Control ====
os.environ["MINERU_BATCH_SIZE"] = "8"
os.environ["PYTORCH_CUDA_ALLOC_CONF"] = "max_split_size_mb:128"

# ==== Disable Visualization ====
os.environ["MINERU_SAVE_VISUALIZATION"] = "False"
os.environ["MINERU_SAVE_INTERMEDIATE"] = "False"


for key in [
    "MINERU_DEVICE",
    "MINERU_USE_GPU",
    "MINERU_USE_FP16",
    "MINERU_SAVE_VISUALIZATION",
    'MINERU_SAVE_INTERMEDIATE',
    'MINERU_MAX_GPU_MEMORY',
]:
    print(f"{key} = {os.getenv(key)}")

def process_pdf(file_name):
    input_path = os.path.join(PATH, file_name)
    result = subprocess.run([
        "mineru",
        "-p", input_path,
        "-o", OUTPUT_PATH,
        "--disable-visualization",
        "--disable-intermediate"
    ], capture_output=True, text=True)

    if result.returncode == 0:
        return f"✅ Success: {file_name}"
    else:
        return f"❌ Failed: {file_name}\n{result.stderr}"



file_names = [f for f in os.listdir(PATH) if f.lower().endswith(".pdf")]
print(file_names)

# with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
#     futures = [executor.submit(process_pdf, f) for f in file_names]
#     for future in as_completed(futures):
#         print(future.result())
#         print()

# file_names = os.listdir(PATH) # [file_name.pdf,...]

# Clean unwanted tables
for file_name in file_names:
    file_name = file_name.replace('.pdf', '')
    file_path = f'Public_test_output/{file_name}/auto'

    with open(f'{file_path}/{file_name}.md', 'r', encoding='utf-8') as f:
        content = f.read()

    cleaned = re.sub(r"<table>.*?VIETTEL AI RACE.*?</table>", "", content, flags=re.S | re.I)
    with open(f'{file_path}/clean_{file_name}.md', 'w', encoding='utf-8') as f:
        f.write(cleaned)


print('BEGIN cleaning markdown')
def clean_markdown(root_dir):
    """
    Clean each markdown file by replace raw heading with markdown heading format
    e.g # 1. -> #, 1.1 -> ##, 1.1.1 -> ### (replace by the dots)
    """
    root_path = Path(root_dir)

    # Iterate through all PublicXXX directories
    for public_dir in sorted(root_path.glob('Public*')):
        if not public_dir.is_dir():
            continue

        main_file = public_dir / 'main.md'
        if not main_file.exists():
            print(f"Skipping {public_dir}: no 'main.md' file found")
            continue

        print(f"Processing {public_dir}")

        # Read the markdown file
        with open(main_file, 'r', encoding='utf-8') as f:
            content = f.read()


        processed_text = process_markdown_comments(content)
        # print(processed_text)

        # Function to convert header notation to markdown headers
        def convert_header(match):
            # Extract the number pattern (e.g., "1", "1.1", "1.2.3")
            header_text = match.group(1)
            # Extract the title (everything after the number series)
            title_text = match.group(2)
            # Count the number of segments (numbers separated by dots)
            # e.g., "1" -> 1 segment, "1.1" -> 2 segments, "1.2.1" -> 3 segments
            # Remove trailing dot if present and count segments
            clean_header = header_text.rstrip('.')
            segments = len(clean_header.split('.'))
            heading_level = segments

            # Return markdown heading with appropriate number of # symbols (number series removed)
            return '#' * heading_level + ' ' + title_text

        # Replace headers like "# 1.", "# 1.1", "# 1.2.1", etc.
        # Pattern: # followed by optional space, then digits and dots, then optional period and space, then capture the title
        cleaned_content = re.sub(r'^# +(\d+(?:\.\d+)*\.?)\s+(.+)$', convert_header, processed_text, flags=re.MULTILINE)

        # Write the cleaned content back to the file
        with open(f'{public_dir}/main.md', 'w', encoding='utf-8') as f:
            f.write(cleaned_content)

        print(f"✓ Cleaned {public_dir}")


def process_markdown_comments(text):
    """
    Adds an underscore to lines that start with '#' but are likely code comments,
    not Markdown headers.

    Args:
        text: A string containing the Markdown content.

    Returns:
        A string with the corrected content.
    """
    processed_lines = []
    lines = text.split('\n')

    for line in lines:
        # We only care about non-empty lines that start with '#'
        stripped_line = line.strip()
        if not stripped_line.startswith('#'):
            processed_lines.append(line)
            continue

        # --- HEURISTIC LOGIC ---
        # A line is considered a code comment if:
        # 1. It contains a Python function definition keyword.
        is_function_def = 'def ' in stripped_line

        # 2. There is no space after the hashes (e.g., "#comment" vs "# header").
        #    This regex checks for one or more '#' followed by a non-space character.
        no_space_after_hash = re.match(r'^#+[^#\s]', stripped_line)

        if is_function_def or no_space_after_hash:
            # This is a code comment, so add an underscore to the original line
            processed_lines.append('_' + line + '_')
        else:
            # This is a legitimate Markdown header, leave it as is
            processed_lines.append(line)

    return '\n'.join(processed_lines)

import os
import shutil
from pathlib import Path

print('BEGIN ORGANIZING DIRECTORY')

def reorganize_directory(root_dir):
    """
    Reorganize directories by moving clean_*.md to main.md and images folder up one level,
    then remove the auto directory.
    """
    root_path = Path(root_dir)

    # Iterate through all PublicXXX directories
    for public_dir in sorted(root_path.glob('Public*')):
        if not public_dir.is_dir():
            continue

        auto_dir = public_dir / 'auto'
        if not auto_dir.exists():
            print(f"Skipping {public_dir}: no 'auto' directory found")
            continue

        print(f"Processing {public_dir}")

        # Find and process clean_*.md file
        for clean_file in auto_dir.glob('clean_*.md'):
            # Rename to main.md and move to parent directory
            new_path = public_dir / 'main.md'
            shutil.move(str(clean_file), str(new_path))
            print(f"  Moved {clean_file.name} to {new_path}")

        # Move images directory if it exists
        images_dir = auto_dir / 'images'
        if images_dir.exists() and images_dir.is_dir():
            new_images_dir = public_dir / 'images'
            if new_images_dir.exists():
                shutil.rmtree(str(new_images_dir))
            shutil.move(str(images_dir), str(public_dir))
            print(f"  Moved images/ to {public_dir}/")

        # Remove the auto directory
        try:
            shutil.rmtree(str(auto_dir))
            print(f"  Removed {auto_dir}/")
        except Exception as e:
            print(f"  Error removing {auto_dir}: {e}")

import os
import shutil
import re
from pathlib import Path

print('BEGIN cleaning markdown')
def clean_markdown(root_dir):
    """
    Clean each markdown file by replace raw heading with markdown heading format
    e.g # 1. -> #, 1.1 -> ##, 1.1.1 -> ### (replace by the dots)
    """
    root_path = Path(root_dir)

    # Iterate through all PublicXXX directories
    for public_dir in sorted(root_path.glob('Public*')):
        if not public_dir.is_dir():
            continue

        main_file = public_dir / 'main.md'
        if not main_file.exists():
            print(f"Skipping {public_dir}: no 'main.md' file found")
            continue

        print(f"Processing {public_dir}")

        # Read the markdown file
        with open(main_file, 'r', encoding='utf-8') as f:
            content = f.read()


        processed_text = process_markdown_comments(content)
        # print(processed_text)

        # Function to convert header notation to markdown headers
        def convert_header(match):
            # Extract the number pattern (e.g., "1", "1.1", "1.2.3")
            header_text = match.group(1)
            # Extract the title (everything after the number series)
            title_text = match.group(2)
            # Count the number of segments (numbers separated by dots)
            # e.g., "1" -> 1 segment, "1.1" -> 2 segments, "1.2.1" -> 3 segments
            # Remove trailing dot if present and count segments
            clean_header = header_text.rstrip('.')
            segments = len(clean_header.split('.'))
            heading_level = segments

            # Return markdown heading with appropriate number of # symbols (number series removed)
            return '#' * heading_level + ' ' + title_text

        # Replace headers like "# 1.", "# 1.1", "# 1.2.1", etc.
        # Pattern: # followed by optional space, then digits and dots, then optional period and space, then capture the title
        cleaned_content = re.sub(r'^# +(\d+(?:\.\d+)*\.?)\s+(.+)$', convert_header, processed_text, flags=re.MULTILINE)

        # Write the cleaned content back to the file
        with open(f'{public_dir}/main.md', 'w', encoding='utf-8') as f:
            f.write(cleaned_content)

        print(f"✓ Cleaned {public_dir}")


def process_markdown_comments(text):
    """
    Adds an underscore to lines that start with '#' but are likely code comments,
    not Markdown headers.

    Args:
        text: A string containing the Markdown content.

    Returns:
        A string with the corrected content.
    """
    processed_lines = []
    lines = text.split('\n')

    for line in lines:
        # We only care about non-empty lines that start with '#'
        stripped_line = line.strip()
        if not stripped_line.startswith('#'):
            processed_lines.append(line)
            continue

        # --- HEURISTIC LOGIC ---
        # A line is considered a code comment if:
        # 1. It contains a Python function definition keyword.
        is_function_def = 'def ' in stripped_line

        # 2. There is no space after the hashes (e.g., "#comment" vs "# header").
        #    This regex checks for one or more '#' followed by a non-space character.
        no_space_after_hash = re.match(r'^#+[^#\s]', stripped_line)

        if is_function_def or no_space_after_hash:
            # This is a code comment, so add an underscore to the original line
            processed_lines.append('_' + line + '_')
        else:
            # This is a legitimate Markdown header, leave it as is
            processed_lines.append(line)

    return '\n'.join(processed_lines)

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
        db_name="gil",
        collection_name="multimodal_rag",
        embed_model="sentence-transformers/paraphrase-multilingual-mpnet-base-v2",
        drop_old=False
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
                doc = Document(page_content=content, metadata=metadata)
                documents.append(doc)

        except Exception as e:
            logger.warning(f"Error converting entity to document: {e}")
            continue

    logger.info(f"Converted {len(documents)} entities to documents")
    return documents

from pathlib import Path
from typing import Dict, Any
import markdown
from bs4 import BeautifulSoup
import re


class MarkdownProcessor:
    """Xử lý file markdown, trích xuất text, bảng, và hình ảnh"""

    def __init__(self, markdown_dir: str, image_base_dir: str):
        self.markdown_dir = Path(markdown_dir)
        self.image_base_dir = Path(image_base_dir)

    def extract_content(self, md_file: Path) -> Dict[str, Any]:
        """Trích xuất text, tables, và images từ markdown"""
        with open(md_file, 'r', encoding='utf-8') as f:
            md_content = f.read()

        html = markdown.markdown(md_content, extensions=['tables', 'fenced_code'])
        soup = BeautifulSoup(html, 'html.parser')

        text_content = soup.get_text(separator='\n', strip=True)

        tables = []
        for table in soup.find_all('table'):
            table_text = table.get_text(separator=' | ', strip=True)
            tables.append(table_text)

        image_paths = []
        img_pattern = r'!\[.*?\]\((.*?)\)'
        for match in re.finditer(img_pattern, md_content):
            img_path = match.group(1).strip()
            if img_path.startswith("images/"):
                full_path = self.markdown_dir / img_path
            else:
                full_path = self.image_base_dir / img_path

            if full_path.exists():
                image_paths.append(str(full_path))

        return {
            'text': text_content,
            'tables': tables,
            'images': image_paths,
            'source': str(md_file)
        }


from typing import Dict, Any, List
from langchain.text_splitter import RecursiveCharacterTextSplitter


class TextEntityProcessor:
    """Xử lý entity text riêng biệt"""

    def __init__(self, text_model, chunk_size=500, overlap=100):
        self.text_model = text_model
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=overlap
        )

    def create_text_entities(self, content: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Tạo text entities"""
        full_text = content['text']

        # Thêm tables vào text nếu có
        if content['tables']:
            full_text += "\n\n" + "\n\n".join(content['tables'])

        text_chunks = self.text_splitter.create_documents([full_text])

        entities = []
        for idx, chunk in enumerate(text_chunks):
            # Text embedding
            text_embedding = self.text_model.encode(chunk.page_content, convert_to_tensor=False).tolist()

            entity = {
                # 'id': f"text_{idx}",
                'content': chunk.page_content,
                'text_dense': text_embedding,  # Dense vector cho semantic search
                'text_sparse': chunk.page_content,  # Text cho BM25 sparse search
                'metadata': {
                    'entity_type': 'text',
                    'source': content['source'],
                    'chunk_index': idx,
                    'content_type': 'text_with_tables' if content['tables'] else 'text_only'
                },
                # Các trường image để trống
                'image_path': '',
                # 'image_caption': '',
                'image_dense': [0.0] * 512  # Vector trống với đúng dimension
            }
            entities.append(entity)

        return entities


class ImageEntityProcessor:
    """Xử lý entity image riêng biệt"""

    def __init__(self, image_encoder):
        self.image_encoder = image_encoder

    def create_image_entities(self, content: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Tạo image entities"""
        entities = []

        for idx, img_path in enumerate(content['images']):
            # Generate caption
            # caption = self.image_encoder.generate_caption(img_path)

            # Multimodal embedding
            image_embedding = self.image_encoder.encode_image_multimodal(img_path)

            # Text embedding của caption (cho text search)
            # caption_embedding = text_model.encode(caption, convert_to_tensor=False).tolist()

            entity = {
                # 'id': f"image_{idx}",
                'content': "",  # Caption làm content chính
                'image_path': img_path,
                # 'image_caption': caption,
                'image_dense': image_embedding,  # Multimodal vector cho image search
                'metadata': {
                    'entity_type': 'image',
                    'source': content['source'],
                    'image_index': idx,
                    'original_path': img_path
                },
                # Các trường text bỏ trống cho image
                'text_dense': [0.0] * 768,  # Dense vector của caption
                # 'text_sparse': caption  # Caption text cho BM25
            }
            entities.append(entity)

        return entities


"""
Milvus Vector Store module for RAG Multimodal application.
This module provides functionality to interact with Milvus vector database for storing and retrieving embeddings.

Usage:
    ```python
    from src.milvus_store import MilvusStore

    # Initialize the vector store
    milvus_store = MilvusStore()

    # Add documents to the vector store
    milvus_store.add_documents(documents)

    # Create a retriever
    retriever = milvus_store.as_retriever(k=3, namespace="custom_namespace")

    # Retrieve documents
    results = retriever.invoke("What is Docling?")
    ```
"""

import os
import logging
from typing import List, Dict, Any, Optional, Union

# Import configuration
from src.config import config

# Import vector store libraries
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_milvus import BM25BuiltInFunction, Milvus
from pymilvus import Collection, MilvusException, connections, db, utility
from langchain_core.documents import Document
from langchain_core.retrievers import BaseRetriever

# Configure logging
logger = logging.getLogger(__name__)

# Default log file path
DEFAULT_LOG_FILE = os.path.join('logs', 'milvus_store.log')


def configure_logging(level=logging.INFO, log_file=None):
    """
    Configure logging for the milvus_store module.

    Args:
        level: Logging level (default: logging.INFO)
        log_file: Path to log file (default: None, logs to console only)
    """
    # Create a formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # Configure the logger
    logger.setLevel(level)

    # Remove existing handlers to avoid duplicates
    for handler in logger.handlers[:]:
        logger.removeHandler(handler)

    # Create console handler and set level
    console_handler = logging.StreamHandler()
    console_handler.setLevel(level)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # Add file handler if log_file is specified
    if log_file:
        try:
            # Create directory for log file if it doesn't exist
            log_dir = os.path.dirname(log_file)
            if log_dir and not os.path.exists(log_dir):
                os.makedirs(log_dir)

            # Create file handler and set level
            file_handler = logging.FileHandler(log_file)
            file_handler.setLevel(level)
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)
            logger.info(f"Logging to file: {log_file}")
        except Exception as e:
            logger.error(f"Failed to set up file logging to {log_file}: {e}")

    logger.debug("Logging configured for milvus_store module")


# Configure logging with default settings
configure_logging(log_file=DEFAULT_LOG_FILE)


def drop_collection(collection_name: str, db_name: str, uri: str = None, token: str = None) -> bool:
    """
    Drop a collection from the specified database.

    Args:
        collection_name: Name of the collection to drop
        db_name: Name of the database containing the collection
        uri: Milvus uri
        token: Authentication token (optional, uses config if not provided)

    Returns:
        bool: True if collection was successfully dropped, False otherwise
    """
    try:
        # Connect if URI and token are provided
        if uri and token:
            host = uri.split("://")[1].split(":")[0]
            port = int(uri.split(":")[-1])
            connections.connect(host=host, port=port)

        # Check if the database exists
        existing_databases = db.list_database()
        if db_name not in existing_databases:
            logger.warning(f"Database '{db_name}' không tồn tại.")
            return False

        # Switch to the specified database
        db.using_database(db_name)

        # Check if the collection exists
        collections = utility.list_collections()
        if collection_name not in collections:
            logger.warning(f"Collection '{collection_name}' không tồn tại trong database '{db_name}'.")
            return False

        # Drop the collection
        collection = Collection(name=collection_name)
        collection.drop()
        logger.info(f"Collection '{collection_name}' đã bị xoá khỏi database '{db_name}'.")
        return True

    except MilvusException as e:
        logger.error(f"Xảy ra lỗi trong quá trình xoá collection: {e}")
        return False


def drop_all_collections(db_name: str, confirm: bool = False, uri: str = None, token: str = None) -> bool:
    """
    Drop all collections in a database.

    Args:
        db_name: Name of the database containing the collections
        confirm: Set to True to confirm the operation (defaults to False)
        uri: Milvus uri
        token: Authentication token (optional, uses config if not provided)

    Returns:
        bool: True if all collections were successfully dropped, False otherwise
    """
    if not confirm:
        logger.warning(f"WARNING: Bạn chuẩn bị xoá toàn bộ collections trong database '{db_name}'")
        logger.warning("Hành động này không thể thu hồi. Đặt confirm=True để tiến hành.")
        return False

    try:
        # Connect if URI and token are provided
        if uri and token:
            host = uri.split("://")[1].split(":")[0]
            port = int(uri.split(":")[-1])
            connections.connect(host=host, port=port)

        # Check if the database exists
        existing_databases = db.list_database()
        if db_name not in existing_databases:
            logger.warning(f"Database '{db_name}' không tồn tại.")
            return False

        # Switch to the specified database
        db.using_database(db_name)

        # Get all collections in the database
        collections = utility.list_collections()
        logger.info(f"Found {len(collections)} collections in database '{db_name}'")

        # Drop each collection
        for collection_name in collections:
            logger.info(f"Dropping collection '{collection_name}'...")
            success = drop_collection(collection_name=collection_name, db_name=db_name, uri=uri, token=token)
            if not success:
                logger.error(f"Failed to drop collection '{collection_name}'")
                return False
            logger.info(f"Successfully dropped collection '{collection_name}'")

        return True

    except MilvusException as e:
        logger.error(f"Error dropping collections: {e}")
        return False


def drop_database(db_name: str, confirm: bool = False, uri: str = None, token: str = None) -> bool:
    """
    Drop a database and all its collections.

    Args:
        db_name: Name of the database to drop
        confirm: Set to True to confirm the operation (defaults to False)
        uri: Milvus uri
        token: Authentication token (optional, uses config if not provided)

    Returns:
        bool: True if database was successfully dropped, False otherwise
    """
    if not confirm:
        logger.warning(f"WARNING: You are about to drop database '{db_name}'")
        logger.warning("This operation is irreversible. Set confirm=True to proceed.")
        return False

    try:
        # Connect if URI and token are provided
        if uri and token:
            host = uri.split("://")[1].split(":")[0]
            port = int(uri.split(":")[-1])
            connections.connect(host=host, port=port)

        # Check if the database exists
        existing_databases = db.list_database()
        if db_name not in existing_databases:
            logger.warning(f"Database '{db_name}' does not exist.")
            return False

        # First drop all collections in the database
        if not drop_all_collections(db_name, confirm=True, uri=uri, token=token):
            logger.error(f"Failed to drop all collections in database '{db_name}'")
            return False

        # Now drop the database
        db.drop_database(db_name)
        logger.info(f"Database '{db_name}' has been dropped.")
        return True

    except MilvusException as e:
        logger.error(f"Error dropping database: {e}")
        return False




class MilvusStore:
    """
    A class to manage interactions with Milvus vector database.

    This class provides functionality to interact with Milvus vector database for storing and retrieving embeddings.
    It includes comprehensive logging capabilities that can be configured using the set_log_level method.

    Logging Features:
    - Console logging (default at INFO level)
    - File logging (default to 'logs/milvus_store.log')
    - Configurable log levels (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    - Formatted log messages with timestamps

    Example:
        ```python
        # Set custom debug level with custom file path
        MilvusStore.set_log_level(logging.DEBUG, 'custom/path/milvus.log')

        # Create store with default logging (INFO level)
        store = MilvusStore()
        ```
    """

    def __init__(
        self,
        uri: str = None,
        db_name: str = None,
        collection_name: str = None,
        embed_model: str = None,
        drop_old: bool = False,
        namespace: str = None
    ):
        """
        Initialize the MilvusStore.

        Args:
            uri: URI for Milvus connection (defaults to config.get("database", "uri"))
            db_name: Name of the database (defaults to config.get("database", "name"))
            collection_name: Name of the collection (defaults to config.get("database", "collection_name"))
            embed_model: Embedding model to use (defaults to config.get("model", "embeddings"))
            drop_old: Whether to drop the existing collection if it exists
            namespace: Default namespace to use for documents (defaults to config.get("database", "namespace"))

        """
        # Local Milvus connection only
        self.uri = uri or config.get("database", "uri", default="http://localhost:19530")
        self.token = None
        self.db_name = db_name or config.get("database", "name", default="gil")
        self.collection_name = collection_name or config.get("database", "collection_name", default="multimodal_rag")
        self.embed_model = embed_model or config.get("model", "embeddings", default="sentence-transformers/paraphrase-multilingual-mpnet-base-v2")
        self.namespace = namespace or config.get("database", "namespace", default="viettel")

        # Connect to Milvus
        self._connect_to_milvus()

        # Initialize the database
        self._initialize_vector_store(drop_old=drop_old)

        # Create embeddings model (Sentence-Transformers)
        self.embeddings_model = HuggingFaceEmbeddings(model_name=self.embed_model)

        # Create vector store
        self.vector_store = self._create_vector_store(drop_old=drop_old)

    def _connect_to_milvus(self) -> None:
        """
        Connect to Milvus server
        """
        # Local Milvus connection
        host = self.uri.split("://")[1].split(":")[0]
        port = int(self.uri.split(":")[-1])
        connections.connect(host=host, port=port)

    def _initialize_vector_store(self, drop_old: bool = False) -> None:
        """
        Initialize the vector store database.

        Args:
            drop_old: Whether to drop the existing database if it exists
        """
        try:
            existing_databases = db.list_database()
            if self.db_name in existing_databases:
                logger.info(f"Database '{self.db_name}' already exists.")

                # Use the database context
                db.using_database(self.db_name)

                if drop_old:
                    # Drop the collection if it exists
                    collections = utility.list_collections()
                    if self.collection_name in collections:
                        drop_collection(self.collection_name, self.db_name)
            else:
                logger.info(f"Database '{self.db_name}' does not exist.")
                db.create_database(self.db_name)
                logger.info(f"Database '{self.db_name}' created successfully.")
        except MilvusException as e:
            logger.error(f"An error occurred: {e}")

    def _create_vector_store(self, drop_old: bool = False) -> Milvus:
        """
        Create and configure a vector store.

        Args:
            drop_old: Whether to drop the existing collection if it exists

        Returns:
            Milvus: Configured vector store
        """
        connection_args = {
            "uri": self.uri,
            "db_name": self.db_name
        }

        # Local only; no token

        # Create and return vector store
        return Milvus(
            embedding_function=self.embeddings_model,
            connection_args=connection_args,
            builtin_function=BM25BuiltInFunction(),
            vector_field=["dense", "sparse"],
            consistency_level="Strong",
            drop_old=drop_old,
            collection_name=self.collection_name,
            auto_id=True,
            partition_key_field="namespace"
        )

    def add_documents(self, documents: List[Document]) -> List[str]:
        """
        Add documents to the vector store.

        Args:
            documents: List of documents to add

        Returns:
            List[str]: List of document IDs
        """
        if not documents:
            logger.warning("No documents to add")
            return []

        try:
            ids = self.vector_store.add_documents(documents=documents)
            logger.info(f"Successfully added {len(ids)} documents")
            return ids
        except Exception as e:
            logger.error(f"Error adding documents: {e}")
            return []

    def _build_filter_expr(self, namespace: Optional[str] = None, source_normalized: Optional[str] = None) -> Optional[str]:
        """
        Tạo biểu thức filter Milvus từ namespace và source_normalized, đồng thời ghi log.
        """
        clauses = []
        if namespace:
            clauses.append(f'namespace == "{namespace}"')
        if source_normalized:
            clauses.append(f'source_normalized == "{source_normalized}"')
        expr = " and ".join(clauses) if clauses else None
        logger.info(f"[MilvusStore] Built filter expr: {expr}")
        return expr

    def as_retriever(
        self,
        k: int = 3,
        namespace: str = None,
        ranker_type: str = "weighted",
        ranker_weights: List[float] = None,
        mmr: bool = True,
        fetch_k: int = 12,
        source_normalized: Optional[str] = None
    ) -> BaseRetriever:
        """
        Tạo retriever áp dụng filter theo namespace/source_normalized nếu cung cấp.
        Lưu ý: retriever dùng expr cố định (không fallback cho từng query).
        """
        namespace = namespace or self.namespace
        ranker_weights = ranker_weights or [0.6, 0.4]

        expr = self._build_filter_expr(namespace=namespace, source_normalized=source_normalized)
        search_kwargs = {
            "k": k,
            "mmr": mmr,
            "fetch_k": fetch_k
        }
        if expr:
            search_kwargs["expr"] = expr
            logger.info(f"[MilvusStore] as_retriever expr={expr}, k={k}, fetch_k={fetch_k}")

        return self.vector_store.as_retriever(
            search_kwargs=search_kwargs,
            ranker_type=ranker_type,
            ranker_params={"weights": ranker_weights}
        )

    def similarity_search(
        self,
        query: str,
        k: int = 4,
        namespace: str = None,
        source: str = None,
        source_normalized: str = None
    ) -> List[Document]:
        """
        Perform a similarity search.

        Args:
            query: Query string
            k: Number of documents to retrieve
            namespace: Namespace to filter by (defaults to self.namespace)

        Returns:
            List[Document]: List of similar documents
        """
        namespace = namespace or self.namespace

        # Thử expr chặt (namespace + source_normalized)
        expr_strict = self._build_filter_expr(namespace=namespace, source_normalized=source_normalized)
        logger.info(f"[MilvusStore] similarity_search expr_strict={expr_strict}, k={k}")
        results = self.vector_store.similarity_search(query, k=k, expr=expr_strict)

        # Fallback: nếu có hint nhưng 0 kết quả, nới lỏng còn namespace (hoặc toàn bộ nếu không có namespace)
        if not results and source_normalized:
            expr_relax = self._build_filter_expr(namespace=namespace, source_normalized=None)
            logger.info(f"[MilvusStore] similarity_search fallback expr_relax={expr_relax}")
            results = self.vector_store.similarity_search(query, k=k, expr=expr_relax)

        logger.info(f"[MilvusStore] similarity_search returned {len(results)} results")
        return results

    def similarity_search_with_score(
        self,
        query: str,
        k: int = 4,
        namespace: str = None,
        source: str = None,
        source_normalized: str = None
    ) -> List[tuple]:
        """
        Perform a similarity search with scores.

        Args:
            query: Query string
            k: Number of documents to retrieve
            namespace: Namespace to filter by (defaults to self.namespace)

        Returns:
            List[tuple]: List of (document, score) tuples
        """
        namespace = namespace or self.namespace

        # Thử expr chặt (namespace + source_normalized)
        expr_strict = self._build_filter_expr(namespace=namespace, source_normalized=source_normalized)
        logger.info(f"[MilvusStore] similarity_search_with_score expr_strict={expr_strict}, k={k}")
        results = self.vector_store.similarity_search_with_score(query, k=k, expr=expr_strict)

        # Fallback: nếu có hint nhưng 0 kết quả, nới lỏng còn namespace (hoặc toàn bộ nếu không có namespace)
        if not results and source_normalized:
            expr_relax = self._build_filter_expr(namespace=namespace, source_normalized=None)
            logger.info(f"[MilvusStore] similarity_search_with_score fallback expr_relax={expr_relax}")
            results = self.vector_store.similarity_search_with_score(query, k=k, expr=expr_relax)

        logger.info(f"[MilvusStore] similarity_search_with_score returned {len(results)} results")
        return results

    @staticmethod
    def set_log_level(level=logging.INFO, log_file=None):
        """
        Set the logging level for the MilvusStore module.

        Args:
            level: Logging level (e.g., logging.DEBUG, logging.INFO, logging.WARNING)
            log_file: Optional path to log file

        Example:
            ```python
            # Set to debug level with file logging
            MilvusStore.set_log_level(logging.DEBUG, 'logs/milvus.log')

            # Set to warning level with console only
            MilvusStore.set_log_level(logging.WARNING)
            ```
        """
        configure_logging(level=level, log_file=log_file)
        logger.info(f"Log level set to: {logging.getLevelName(level)}")

    def drop_collection(self, collection_name: str = None, db_name: str = None) -> bool:
        """
        Drop a collection from the specified database.

        Args:
            collection_name: Name of the collection to drop (defaults to self.collection_name)
            db_name: Name of the database containing the collection (defaults to self.db_name)

        Returns:
            bool: True if collection was successfully dropped, False otherwise
        """
        collection_name = collection_name or self.collection_name
        db_name = db_name or self.db_name

        return drop_collection(collection_name, db_name, self.uri, self.token)

    def drop_all_collections(self, db_name: str = None, confirm: bool = False) -> bool:
        """
        Drop all collections in a database.

        Args:
            db_name: Name of the database containing the collections (defaults to self.db_name)
            confirm: Set to True to confirm the operation (defaults to False)

        Returns:
            bool: True if all collections were successfully dropped, False otherwise
        """
        db_name = db_name or self.db_name

        return drop_all_collections(db_name, confirm, self.uri, self.token)

    def drop_database(self, db_name: str = None, confirm: bool = False) -> bool:
        """
        Drop a database and all its collections.

        Args:
            db_name: Name of the database to drop (defaults to self.db_name)
            confirm: Set to True to confirm the operation (defaults to False)

        Returns:
            bool: True if database was successfully dropped, False otherwise
        """
        db_name = db_name or self.db_name

        return drop_database(db_name, confirm, self.uri, self.token)

from pymilvus import AnnSearchRequest, RRFRanker
from typing import List, Dict
import torch

device = "cuda" if torch.cuda.is_available() else "cpu"


class HybridSearchEngine:
    """Engine cho hybrid search với multiple vectors từ text input"""

    def __init__(self, milvus_store, text_model, image_encoder):
        self.store = milvus_store
        self.text_model = text_model
        self.image_encoder = image_encoder

    def hybrid_search(self, query_text: str, limit: int = 10) -> List[Dict]:
        """Thực hiện hybrid search chỉ với text input"""

        search_requests = []

        if not query_text:
            return []

        # 1. Text semantic search với text embedding model
        query_text_embedding = self.text_model.encode(query_text, convert_to_tensor=True, device=device).tolist()

        text_search = AnnSearchRequest(
            data=[query_text_embedding],
            anns_field="text_dense",
            param={"nprobe": 10},
            limit=limit
        )
        search_requests.append(text_search)

        # 2. Full-text search (BM25) với sparse vectors
        sparse_search = AnnSearchRequest(
            data=[query_text],
            anns_field="text_sparse",
            param={"drop_ratio_search": 0.2},
            limit=limit
        )
        search_requests.append(sparse_search)

        # 3. Multimodal search - embedding text bằng image encoder
        query_image_embedding = self.image_encoder.encode_text_for_image_search(query_text)

        image_search = AnnSearchRequest(
            data=[query_image_embedding],
            anns_field="image_dense",
            param={"nprobe": 10},
            limit=limit
        )
        search_requests.append(image_search)

        # Thực hiện hybrid search với RRF ranker
        ranker = RRFRanker(100)

        results = self.store.client.hybrid_search(
            collection_name=self.store.collection_name,
            reqs=search_requests,
            ranker=ranker,
            limit=limit,
            output_fields=["content", "metadata", "image_path"]
        )

        return results[0] if results else []

import os


def write_answers_to_file(answers):
    print('Write TASK QA')
    with open('answer.md', 'a') as f:
        f.write("\n\n### TASK QA\n")
        f.write("num_correct,answers\n")
        for answer in answers:
            # Split by comma and strip spaces to count options
            options = [opt.strip() for opt in answer.split(',')]
            num_correct = len(options)
            # Format as required, quote if multiple
            if num_correct == 1:
                f.write(f"{num_correct},{answer}\n")
            else:
                f.write(f"{num_correct},\"{answer}\"\n")


def write_extract_to_file(extracted_folder, debug=False):
    print('Write TASK EXTRACT')
    file_names = [d for d in os.listdir(extracted_folder) if os.path.isdir(os.path.join(extracted_folder, d))]
    print(file_names)

    with open('temp_answer.md', 'w', encoding='utf-8') as f:
        f.write('### TASK EXTRACT')

    if debug:
        for i, file_name in enumerate(file_names[:2]):
            MARKDOWN_DIR = os.path.join(extracted_folder, file_name)
            # print('MARKDOWN_DIR:', MARKDOWN_DIR)

            with open(f'{MARKDOWN_DIR}/main.md', 'r', encoding='utf-8') as f:
                content = f.read()
            with open('temp_answer.md', 'a', encoding='utf-8') as f:
                f.write(f'\n\n# {file_name[:6]}_{file_name[-3:]} {content}')
    else:
        for i, file_name in enumerate(file_names):
            MARKDOWN_DIR = os.path.join(extracted_folder, file_name)
            # print('MARKDOWN_DIR:', MARKDOWN_DIR)

            with open(f'{MARKDOWN_DIR}/main.md', 'r', encoding='utf-8') as f:
                content = f.read()
            with open('temp_answer.md', 'a', encoding='utf-8') as f:
                f.write(f'\n\n# {file_name[:6]}_{file_name[-3:]} {content}')



    # Move content from temp_answer.md to answer.md
    with open('temp_answer.md', 'r', encoding='utf-8') as temp_f:
        temp_content = temp_f.read()
    with open('answer.md', 'w', encoding='utf-8') as f:
        f.write(temp_content)
    os.remove('temp_answer.md')


"""
Configuration file for RAG Multimodal application.
Contains all the configuration parameters used across the application.

Usage:
    ```python
    from src.config import config

    # Access configuration values by path
    model = config.get("model", "text_generation", default="gpt-4.1-mini")
    embed_model = config.get("model", "embeddings", default="text-embedding-3-small")

    # Get specialized configuration objects
    milvus_args = config.get_milvus_connection_args()
    pdf_options = config.get_pdf_pipeline_options()

    # Use custom configuration file
    from src.config import ConfigLoader
    custom_config = ConfigLoader("path/to/custom/config.yaml")
    custom_model = custom_config.get("model", "text_generation")

    # Strict mode - prevent accidental new key creation
    strict_config = ConfigLoader(allow_new_keys=False)
    strict_config.set("model", "text_generation", "gpt-4")  # OK - existing key
    # strict_config.set("new", "key", "value")  # Would raise KeyError
    strict_config.set("new", "key", "value", force=True)  # OK - forced
    ```
"""
import os
import yaml
from pathlib import Path
from typing import Dict, Any, Optional, Union
# from dotenv import load_dotenv

class ConfigLoader:
    """Configuration loader for RAG Multimodal application"""

    def __init__(self, config_path: Optional[Union[str, Path]] = None, allow_new_keys: bool = True):
        """Initialize ConfigLoader with optional custom config path

        Args:
            config_path: Optional path to configuration file
            allow_new_keys: Whether to allow setting keys that don't exist in the original config
        """
        self._config = None
        self._allow_new_keys = allow_new_keys
        self._load_config(config_path)

    def _load_config(self, config_path: Optional[Union[str, Path]] = None):
        """Load configuration from YAML file and environment variables"""
        # # Load environment variables
        # env_path = Path(__file__).parent.parent / ".env"
        # load_dotenv(env_path)

        # Determine config file path
        if config_path:
            yaml_path = Path(config_path)
            print('yaml_path-default:', yaml_path)
        else:
            yaml_path = Path(__file__).parent.parent / "config.yaml"
            print('yaml_path-else:', yaml_path)

        if yaml_path.exists():
            print('yaml_path:', yaml_path)
            with open(yaml_path, 'r', encoding='utf-8') as file:
                self._config = yaml.safe_load(file)
        else:
            raise FileNotFoundError(f"Configuration file not found: {yaml_path}")

    @property
    def config(self) -> Dict[str, Any]:
        """Get the loaded configuration"""
        return self._config or {}

    def get(self, *keys, default=None) -> Any:
        """Get a configuration value by key path"""
        value = self._config
        for key in keys:
            if isinstance(value, dict) and key in value:
                value = value[key]
            else:
                return default
        return value

    def set(self, *keys_and_value, force: bool = False) -> None:
        """Set a configuration value by key path

        Args:
            *keys_and_value: Key path followed by the value to set
                           Last argument is the value, preceding arguments are the key path
            force: If True, allows setting new keys even when allow_new_keys is False

        Example:
            config.set("model", "text_generation", "gpt-4")
            config.set("database", "uri", "http://localhost:19530")
            config.set("new", "key", "value", force=True)  # Force creation of new key

        Raises:
            KeyError: If trying to set a non-existing key when allow_new_keys is False
        """
        if len(keys_and_value) < 2:
            raise ValueError("At least one key and a value must be provided")

        # Split keys and value
        keys = keys_and_value[:-1]
        value = keys_and_value[-1]

        # Initialize config if None
        if self._config is None:
            self._config = {}

        # Check if we're allowed to create new keys
        if not self._allow_new_keys and not force:
            self._validate_key_exists(keys)

        # Navigate to the parent of the target key
        current = self._config
        for key in keys[:-1]:
            if key not in current:
                if not self._allow_new_keys and not force:
                    raise KeyError(f"Key path {'.'.join(keys)} does not exist and allow_new_keys is False. Use force=True to override.")
                current[key] = {}
            elif not isinstance(current[key], dict):
                # Convert non-dict values to dict to allow nested setting
                current[key] = {}
            current = current[key]

        # Check final key
        if keys[-1] not in current and not self._allow_new_keys and not force:
            raise KeyError(f"Key '{keys[-1]}' does not exist in path {'.'.join(keys[:-1])} and allow_new_keys is False. Use force=True to override.")

        # Set the final value
        current[keys[-1]] = value

    def _validate_key_exists(self, keys) -> None:
        """Validate that a key path exists in the configuration

        Args:
            keys: Key path to validate

        Raises:
            KeyError: If the key path doesn't exist
        """
        current = self._config
        for i, key in enumerate(keys):
            if not isinstance(current, dict) or key not in current:
                key_path = '.'.join(keys[:i+1])
                raise KeyError(f"Key path '{key_path}' does not exist and allow_new_keys is False. Use force=True to override.")
            current = current[key]

    def reload(self, config_path: Optional[Union[str, Path]] = None) -> None:
        """Reload configuration from file"""
        self._load_config(config_path)

    def set_allow_new_keys(self, allow: bool) -> None:
        """Set whether new keys are allowed to be created

        Args:
            allow: Whether to allow creation of new keys
        """
        self._allow_new_keys = allow

    def get_allow_new_keys(self) -> bool:
        """Get whether new keys are allowed to be created

        Returns:
            bool: Current allow_new_keys setting
        """
        return self._allow_new_keys

    def get_milvus_connection_args(self) -> Dict[str, str]:
        """Get Milvus connection arguments (local docker-compose)."""
        return {
            "uri": self.get("database", "uri", default="http://localhost:19530"),
            "db_name": self.get("database", "name", default="gil")
        }

    def get_pdf_pipeline_options(self) -> Dict[str, Any]:
        """Get PDF pipeline options"""
        from docling.datamodel.pipeline_options import (
            PdfPipelineOptions,
            PictureDescriptionApiOptions
        )

        # Get API configuration (Ollama OpenAI-compatible or disabled)
        base_url = self.get("model", "url", default="http://localhost:11434/v1")
        model_name = self.get("model", "text_generation", default="")
        vision_model = self.get("model", "vision_model", default="")
        model_timeout = self.get("model", "timeout", default=60)
        picture_prompt = self.get("document", "picture_description", "prompt_picture_description",
                                default="Describe this image in sentences in a single paragraph.")
        pd_enabled = bool(self.get("document", "picture_description", "enabled", default=True))
        image_scale = self.get("document", "image_resolution_scale", default=2)

        # Nếu tắt picture description, không cấu hình remote API
        if not pd_enabled:
            return PdfPipelineOptions(
                images_scale=image_scale,
                generate_picture_images=False,
                do_picture_description=False,
                picture_description_options=None,
                enable_remote_services=False,
            )

        # Dùng vision_model nếu có, fallback sang model_name
        pd_model = vision_model if vision_model else model_name
        headers = {}

        picture_desc_api_option = PictureDescriptionApiOptions(
            url=f"{base_url}/chat/completions" if not base_url.endswith("/chat/completions") and not base_url.endswith("/v1/chat/completions") else base_url,
            prompt=picture_prompt,
            params={"model": pd_model},
            headers=headers,
            timeout=model_timeout,
        )

        return PdfPipelineOptions(
            images_scale=image_scale,
            generate_picture_images=True,
            do_picture_description=True,
            picture_description_options=picture_desc_api_option,
            enable_remote_services=True,
        )

# Create a default configuration instance
config = ConfigLoader()


import logging
import os
import time
import uuid
from typing import Dict, List, Literal, Any, Optional, Union
import re
import csv
import json

# Import configuration
from src.config import config

# Import LangGraph components
from langgraph.graph import StateGraph, MessagesState, START, END
from langgraph.prebuilt import ToolNode
# Removed tools_condition import as we use custom routing
from langgraph.checkpoint.memory import InMemorySaver

# Import LangChain components
from langchain_core.messages import convert_to_messages, HumanMessage
from langchain_openai import ChatOpenAI
from langchain.tools.retriever import create_retriever_tool
from pydantic import BaseModel, Field

# Import Milvus store
from src.milvus_store import MilvusStore
# Configure logging
logger = logging.getLogger(__name__)
# Default log file path
DEFAULT_LOG_FILE = 'logs/agent.log'

def configure_logging(level=logging.INFO, log_file=None):
    """
    Configure logging for the agent module.
    Args:
        level: Logging level (default: logging.INFO)
        log_file: Path to log file (default: None, logs to console only)
    """
    # Create a formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    # Configure the logger
    logger.setLevel(level)
    # Remove existing handlers to avoid duplicates
    for handler in logger.handlers[:]:
        logger.removeHandler(handler)
    # Create console handler and set level
    console_handler = logging.StreamHandler()
    console_handler.setLevel(level)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # Add file handler if log_file is specified
    if log_file:
        try:
            # Create directory for log file if it doesn't exist
            import os
            log_dir = os.path.dirname(log_file)
            if log_dir and not os.path.exists(log_dir):
                os.makedirs(log_dir)

            # Create file handler and set level
            file_handler = logging.FileHandler(log_file)
            file_handler.setLevel(level)
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)
            logger.info(f"Logging to file: {log_file}")
        except Exception as e:
            logger.error(f"Failed to set up file logging to {log_file}: {e}")
        # Trace file logging disabled per user request; only logging to agent.log and console
    logger.debug("Logging configured for agent module")

# Configure logging with default settings
configure_logging(log_file=DEFAULT_LOG_FILE)

def generate_thread_id() -> str:
    """
    Generate a unique thread ID using timestamp and UUID.
    Returns:
        str: Unique thread ID in format "{timestamp}_{random_uuid}"
    """
    timestamp = str(int(time.time() * 1000))  # milliseconds
    random_uuid = str(uuid.uuid4()).replace('-', '')  # 8 chars from UUID
    return f"{timestamp}_{random_uuid}"

class GradeDocuments(BaseModel):
    """Grade documents using a binary score for relevance check."""
    binary_score: str = Field(
        description="Relevance score: 'yes' if relevant, or 'no' if not relevant"
    )
class ExtractSourceHint(BaseModel):
    """Structured extraction of a potential document/file hint from the question."""
    source_hint: Optional[str] = Field(default=None, description="Document/file name if mentioned; otherwise null")

class MCQAnswer(BaseModel):
    """Structured answer for multiple-choice questions."""
    thinking: str = Field(description="Quá trình suy nghĩ chi tiết bằng tiếng Việt")
    rationale: str = Field(description="Giải thích ngắn gọn bằng tiếng Việt")
    final_answer: str = Field(description="Các đáp án đúng dạng chữ cái, ví dụ: 'A' hoặc 'A,B'")

class AgenticRAG:
    """
    Agentic RAG implementation using LangGraph.

    This class implements an agentic RAG system that uses a graph-based approach to:
    1. Generate a query or respond directly
    2. Retrieve relevant documents from multiple vector stores
    3. Grade document relevance
    4. Rewrite the question if needed
    5. Generate a final answer

    The system supports multiple vector stores, each converted to a retriever tool that
    the agent can access. Uses LangGraph for orchestrating the RAG workflow.
    """
    def __init__(
            self,
            vector_stores: Optional[List[Dict[str, Any]]] = None,
            vector_store: Optional[MilvusStore] = None,  # Backward compatibility
            model_name: str = None,
            temperature: float = 0,
            thread_id: Optional[str] = None,
            checkpointer: Optional[InMemorySaver] = None,
        ):
        """
        Initialize the AgenticRAG system.

        Args:
            vector_stores: List of vector store configurations. Each dict should contain:
							- 'store': MilvusStore instance
							- 'name': Tool name (string)
							- 'description': Tool description (string)
							- 'k': Optional retrieval count (defaults to config)
							- 'ranker_weights': Optional ranker weights (defaults to config)
            vector_store: Single MilvusStore instance for backward compatibility
            model_name: Name of the model to use (defaults to config.get("model", "text_generation"))
            temperature: Temperature for the model (default: 0)
            thread_id: Optional thread ID for the conversation (default: None)
            checkpointer: Optional checkpointer for saving the conversation state (default: None)
        """
        self.model_name = model_name or config.get("model", "text_generation", default="qwen2.5:latest")
        self.temperature = temperature
        self.checkpointer = checkpointer or InMemorySaver()
        # Generate unique thread_id if not provided
        if thread_id is None:
            self.thread_id = generate_thread_id()
        else:
            self.thread_id = thread_id
        # Initialize vector stores and create retriever tools
        self.vector_stores = []
        self.retriever_tools = []

        if vector_stores:
            # Use the new multiple vector stores approach
            for vs_config in vector_stores:
                if not isinstance(vs_config, dict):
                    raise ValueError("Each vector store configuration must be a dictionary")

                required_keys = ['store', 'name', 'description']
                missing_keys = [key for key in required_keys if key not in vs_config]
                if missing_keys:
                    raise ValueError(f"Vector store configuration missing required keys: {missing_keys}")

                store = vs_config['store']
                name = vs_config['name']
                description = vs_config['description']
                k = vs_config.get('k', config.get("retrieval", "k", default=2))
                ranker_weights = vs_config.get('ranker_weights', config.get("retrieval", "weights", default=[0.6, 0.4]))
                # Create retriever
                retriever = store.as_retriever(k=k, ranker_weights=ranker_weights)
                # Create retriever tool
                retriever_tool = create_retriever_tool(retriever, name, description)
                # Store the configuration
                self.vector_stores.append({
                    'store': store,
                    'name': name,
                    'description': description,
                    'retriever': retriever,
                    'tool': retriever_tool,
                    'k': k,
                    'ranker_weights': ranker_weights
                })
                self.retriever_tools.append(retriever_tool)

        elif vector_store:
            # Backward compatibility: single vector store
            retriever = vector_store.as_retriever(
                k=config.get("retrieval", "k", default=6),
                ranker_weights=config.get("retrieval", "weights", default=[0.6, 0.4])
            )
            retriever_tool = create_retriever_tool(
                retriever,
                "retrieve_documents",
                "Search and retrieve information from the document collection."
            )
            self.vector_stores.append({
                'store': vector_store,
                'name': 'retrieve_documents',
                'description': 'Search and retrieve information from the document collection.',
                'retriever': retriever,
                'tool': retriever_tool,
                'k': config.get("retrieval", "k", default=2),
                'ranker_weights': config.get("retrieval", "weights", default=[0.6, 0.4])
            })
            self.retriever_tools.append(retriever_tool)
        else:
            # Default: create a single MilvusStore (local Milvus)
            default_store = MilvusStore()
            retriever = default_store.as_retriever(
                k=config.get("retrieval", "k", default=6),
                ranker_weights=config.get("retrieval", "weights", default=[0.6, 0.4])
            )
            retriever_tool = create_retriever_tool(
                retriever,
                "retrieve_documents",
                "Search and retrieve information from the document collection."
            )
            self.vector_stores.append({
                'store': default_store,
                'name': 'retrieve_documents',
                'description': 'Search and retrieve information from the document collection.',
                'retriever': retriever,
                'tool': retriever_tool,
                'k': config.get("retrieval", "k", default=2),
                'ranker_weights': config.get("retrieval", "weights", default=[0.6, 0.4])
            })
            self.retriever_tools.append(retriever_tool)
        # Maintain backward compatibility attributes
        self.vector_store = self.vector_stores[0]['store'] if self.vector_stores else None
        self.retriever = self.vector_stores[0]['retriever'] if self.vector_stores else None
        self.retriever_tool = self.retriever_tools[0] if self.retriever_tools else None
        # Initialize the LLM via Ollama (OpenAI-compatible API)
        base_url = config.get("model", "url", default="http://localhost:11434/v1")
        # ChatOpenAI requires an api_key field; any non-empty string works for Ollama
        self.response_model = ChatOpenAI(
            model=self.model_name,
            temperature=self.temperature,
            base_url=base_url,
            api_key="ollama",
            top_p= 0.1
        )
        self.grader_model = ChatOpenAI(
            model=self.model_name,
            temperature=0,
            base_url=base_url,
            api_key="ollama",
            top_p= 0.1
        )
        # Create the graph
        self.graph = self._build_graph()

        logger.info(f"AgenticRAG initialized with model: {self.model_name} and {len(self.vector_stores)} vector store(s)")

    def add_vector_store(self, store: MilvusStore, name: str, description: str,
                        k: Optional[int] = None, ranker_weights: Optional[List[float]] = None) -> None:
        """
        Add a new vector store to the agent.

        Args:
            store: MilvusStore instance
            name: Tool name for the retriever
            description: Tool description for the retriever
            k: Optional retrieval count (defaults to config)
            ranker_weights: Optional ranker weights (defaults to config)
        """
        k = k or config.get("retrieval", "k", default=2)
        ranker_weights = ranker_weights or config.get("retrieval", "weights", default=[0.6, 0.4])
        # Create retriever
        retriever = store.as_retriever(k=k, ranker_weights=ranker_weights)
        # Create retriever tool
        retriever_tool = create_retriever_tool(retriever, name, description)
        # Store the configuration
        vs_config = {
            'store': store,
            'name': name,
            'description': description,
            'retriever': retriever,
            'tool': retriever_tool,
            'k': k,
            'ranker_weights': ranker_weights
        }
        self.vector_stores.append(vs_config)
        self.retriever_tools.append(retriever_tool)
        # Rebuild the graph to include the new tool
        self.graph = self._build_graph()
        logger.info(f"Added vector store '{name}' to AgenticRAG")
    def remove_vector_store(self, name: str) -> bool:
        """
        Remove a vector store by name.

        Args:
            name: Name of the vector store to remove

        Returns:
            bool: True if removed successfully, False if not found
        """
        for i, vs_config in enumerate(self.vector_stores):
            if vs_config['name'] == name:
                # Remove from both lists
                removed_config = self.vector_stores.pop(i)
                self.retriever_tools.pop(i)
                # Update backward compatibility attributes if needed
                if self.vector_store == removed_config['store']:
                    self.vector_store = self.vector_stores[0]['store'] if self.vector_stores else None
                    self.retriever = self.vector_stores[0]['retriever'] if self.vector_stores else None
                    self.retriever_tool = self.retriever_tools[0] if self.retriever_tools else None
                # Rebuild the graph
                self.graph = self._build_graph()
                logger.info(f"Removed vector store '{name}' from AgenticRAG")
                return True
        logger.warning(f"Vector store '{name}' not found")
        return False

    def get_vector_store_info(self) -> List[Dict[str, Any]]:
        """
        Get information about all configured vector stores.

        Returns:
            List[Dict]: List of vector store information (excluding the actual store and tool objects)
        """
        return [{
            'name': vs['name'],
            'description': vs['description'],
            'k': vs['k'],
            'ranker_weights': vs['ranker_weights']
        } for vs in self.vector_stores]
    def _route_tools(self, state: MessagesState) -> str:
        """
        Custom routing function to route to the appropriate tool node or END.

        Use in the conditional_edge to route to the specific ToolNode if the last message
        has tool calls. Otherwise, route to the end.

        Args:
            state: Current state containing messages

        Returns:
            str: Node name to route to (tool name or END)
        """
        if isinstance(state, list):
            ai_message = state[-1]
        elif messages := state.get("messages", []):
            ai_message = messages[-1]
        else:
            raise ValueError(f"No messages found in input state to tool_edge: {state}")

        if hasattr(ai_message, "tool_calls") and len(ai_message.tool_calls) > 0:
            # Get the tool name from the first tool call
            tool_name = ai_message.tool_calls[0]["name"]

            # Verify that the tool name corresponds to one of our vector store tools
            valid_tool_names = [vs['name'] for vs in self.vector_stores]
            if tool_name in valid_tool_names:
                return tool_name
            else:
                logger.warning(f"Unknown tool name: {tool_name}. Available tools: {valid_tool_names}")
                return END
        return END

    def _build_graph(self) -> StateGraph:
        """
        Build the LangGraph for the agentic RAG system.

        Returns:
            StateGraph: Compiled graph for the RAG workflow
        """
        # Create the workflow
        workflow = StateGraph(MessagesState)
        # Add nodes
        workflow.add_node("generate_query_or_respond", self._generate_query_or_respond)
        # Add each retriever tool as an individual node
        retriever_node_names = []
        for vs_config in self.vector_stores:
            node_name = vs_config['name']
            retriever_node_names.append(node_name)
            workflow.add_node(node_name, ToolNode([vs_config['tool']]))

        workflow.add_node("rewrite_question", self._rewrite_question)
        workflow.add_node("generate_answer", self._generate_answer)
        # Add edges
        workflow.add_edge(START, "generate_query_or_respond")
        # Decide whether to retrieve - map each tool name to its corresponding node
        tools_mapping = {}
        for vs_config in self.vector_stores:
            tool_name = vs_config['name']
            tools_mapping[tool_name] = tool_name
        tools_mapping[END] = END

        workflow.add_conditional_edges(
            "generate_query_or_respond",
            self._route_tools,
            tools_mapping,
        )
        # Grade documents after retrieval from each retriever node
        for node_name in retriever_node_names:
            workflow.add_conditional_edges(
                node_name,
                self._grade_documents,
            )
        workflow.add_edge("generate_answer", END)
        workflow.add_edge("rewrite_question", "generate_query_or_respond")
        # Compile the graph
        graph = workflow.compile(checkpointer=self.checkpointer)
        output_file = "graph.png"
        graph.get_graph().draw_mermaid_png(output_file_path=output_file)
        return graph

    def _generate_query_or_respond(self, state: MessagesState) -> Dict:
        """
        Call the model to generate a response based on the current state.
        Given the input messages, it will decide to retrieve using the retriever tool,
        or respond directly to the user.

        Args:
            state: Current state containing messages

        Returns:
            Dict: Updated state with new messages
        """
        logger.debug("Generating query or response")
        logger.info("[trace] _generate_query_or_respond called")
        # Extract source hint from ORIGINAL question (first user message) to avoid losing it during rewrite
        source_hint = None
        source_hint_norm = None
        try:
            # Get the first user message (original question)
            first_user_msg = None
            messages = state.get("messages", [])
            logger.info(f"[trace] state.messages count: {len(messages)}")
            logger.info(f"[trace] DEBUG: Starting source hint extraction...")
            for i, m in enumerate(messages):
                # Debug message structure
                logger.info(f"[trace] message[{i}] type={type(m)}")
                logger.info(f"[trace] message[{i}] dir={[attr for attr in dir(m) if not attr.startswith('_')]}")
                # Try different ways to get role
                role = None
                if hasattr(m, 'role'):
                    role = m.role
                elif hasattr(m, 'type'):
                    role = m.type
                elif isinstance(m, dict):
                    role = m.get('role', 'unknown')
                logger.info(f"[trace] message[{i}] role={role}")
                if role in ["user", "human"]:
                    first_user_msg = m
                    logger.info(f"[trace] DEBUG: Found user message at index {i} with role={role}")
                    logger.info(f"[trace] DEBUG: first_user_msg type: {type(first_user_msg)}")
                    logger.info(f"[trace] DEBUG: first_user_msg has content: {hasattr(first_user_msg, 'content')}")
                    if hasattr(first_user_msg, 'content'):
                        logger.info(f"[trace] DEBUG: first_user_msg.content type: {type(first_user_msg.content)}")
                        logger.info(f"[trace] DEBUG: first_user_msg.content preview: {str(first_user_msg.content)[:100]}...")
                    break
            if first_user_msg:
                # Try different ways to get content
                content = None
                if hasattr(first_user_msg, 'content'):
                    content = first_user_msg.content
                elif isinstance(first_user_msg, dict):
                    content = first_user_msg.get('content', '')
                if content and isinstance(content, str):
                    original_question = content
                    logger.info(f"[trace] original_question={original_question[:100]}...")
                    # Try LLM extraction first - SIMPLIFIED PROMPT
                    hint_prompt = (
                        "Bạn là một bộ phân tích câu hỏi. Nếu trong câu hỏi có đề cập đến tên tài liệu hoặc tệp cụ thể (ví dụ: Public001, Public_001, Public001.pdf, bài báo Public003, tài liệu Public002), hãy trích xuất và trả về chính xác tên đó (giữ nguyên số, ký tự, hoặc phần mở rộng). Nếu không có, hãy trả về chuỗi rỗng. Chỉ trả về đúng tên tệp hoặc chuỗi rỗng, không thêm bất kỳ giải thích nào.\n"
                        f"Câu hỏi: {original_question}.\n"
                        "Tên tài liệu:"
                    )
                    try:
                        hint_resp = (
                            self.response_model
                            .with_structured_output(ExtractSourceHint)
                            .invoke([{"role": "user", "content": hint_prompt}])
                        )
                        if hint_resp and getattr(hint_resp, 'source_hint', None):
                            raw_hint = str(hint_resp.source_hint).strip().strip('"\'')
                            # Validate: should be short document name, not full question
                            if len(raw_hint) < 50 and any(char.isdigit() for char in raw_hint):
                                source_hint = raw_hint
                                logger.info(f"[trace] source_hint(by-llm)={source_hint}")
                            else:
                                logger.warning(f"[trace] LLM returned invalid source_hint (too long or no digits): {raw_hint[:50]}...")
                                source_hint = None
                    except Exception as e:
                        logger.warning(f"[trace] LLM failed to extract source hint: {e}")
                    # Fallback: regex patterns
                    if not source_hint:
                        patterns = [
                            r"dựa vào tài liệu\s+([\w\-_. ]+)",
                            r"theo\s+tài liệu\s+([\w\-_. ]+)",
                            r"tài liệu\s+([\w\-_. ]+)",
                            r"bài báo\s+([\w\-_. ]+)",
                            r"trong\s+tài liệu\s+([\w\-_. ]+)",
                            r"([A-Za-z]+\d+)",  # Catch patterns like Public002, Public003, etc.
                            r"([A-Za-z]+_\d+)",  # Catch patterns like Public_002, etc.
                        ]
                        for p in patterns:
                            m = re.search(p, original_question, flags=re.IGNORECASE)
                            if m:
                                source_hint = m.group(1).strip().strip('"\'')
                                logger.info(f"[trace] source_hint(by-regex)={source_hint}")
                                break
                    # Normalize source hint
                    if source_hint:
                        base = source_hint.lower().replace('.pdf', '')
                        source_hint_norm = re.sub(r"[^a-z0-9]", "", base)
                        logger.info(f"[trace] source_hint_norm={source_hint_norm}")
        except Exception as e:
            logger.warning(f"[trace] Failed to extract source hint: {e}")

        # Update retriever expr dynamically to include source filter if hinted
        if self.retriever_tools and self.vector_stores:
            for vs in self.vector_stores:
                retriever = vs.get('retriever')
                if retriever and hasattr(retriever, 'search_kwargs'):
                    ns = None
                    # Try to keep existing namespace expression if present in expr or config
                    if 'expr' in retriever.search_kwargs and isinstance(retriever.search_kwargs['expr'], str):
                        # Extract namespace if present
                        ns_match = re.search(r'namespace\s*==\s*"([^"]+)"', retriever.search_kwargs['expr'])
                        if ns_match:
                            ns = ns_match.group(1)
                    if ns is None:
                        ns = getattr(self, 'namespace', None)

                    if source_hint or source_hint_norm:
                        # Chỉ sử dụng source_normalized để lọc, bỏ qua namespace và source
                        if source_hint_norm:
                            retriever.search_kwargs['expr'] = f'source_normalized == "{source_hint_norm}"'
                            logger.info(f"[trace] retriever.expr={retriever.search_kwargs['expr']}")
                    else:
                        # Reset to no filter if we previously set source
                        if 'expr' in retriever.search_kwargs:
                            retriever.search_kwargs.pop('expr', None)
                        logger.info(f"[trace] retriever.expr={retriever.search_kwargs.get('expr', 'None')}")

                    # Thêm log để debug
                    logger.info(f"[trace] search_kwargs={retriever.search_kwargs}")
                    logger.info(f"[trace] source_hint_norm={source_hint_norm}")
                    logger.info(f"[trace] using_namespace=False")
                    # Lưu ý: retriever dùng expr cố định, không tự fallback theo query
                    logger.info(f"[trace] retriever_fallback_enabled=False")

        # Extract MCQ options from ORIGINAL question and inject into state
        augmented_messages = state["messages"]
        try:
            # Use the same first_user_msg we found earlier
            if first_user_msg:
                options = {}
                if hasattr(first_user_msg, 'content'):
                    content = first_user_msg.content
                elif isinstance(first_user_msg, dict):
                    content = first_user_msg.get('content', '')

                if content and isinstance(content, str):
                    # Extract lines like A:, B:, C:, D:
                    for key in ["A", "B", "C", "D"]:
                        mopt = re.search(rf"\b{key}\s*[:\-]\s*(.+)", content, flags=re.IGNORECASE)
                        if mopt:
                            options[key] = mopt.group(1).strip()

                if options:
                    logger.info(f"[trace] mcq_options_detected={list(options.keys())}")
                    # Build combined query hint
                    combined = [f"Question: {content}"]
                    opt_str = "; ".join([f"{k}) {v}" for k, v in options.items()])
                    combined.append(f"Options: {opt_str}")
                    hint = " \n".join(combined)
                    augmented_messages = [{"role": "system", "content": "When you call the retrieval tool, pass the combined query including both the question and the options to maximize matching."}] + augmented_messages + [{"role": "system", "content": f"Combined retrieval query hint:\n{hint}"}]
                else:
                    logger.info("[trace] mcq_options_detected=[]")

        except Exception as e:
            logger.warning(f"[trace] Failed to extract MCQ options: {e}")

        response = (
            self.response_model
            .bind_tools(self.retriever_tools)
            .invoke(augmented_messages)
        )
        # FORCE tool calling for MCQ RAG - always retrieve documents
        if not (hasattr(response, "tool_calls") and response.tool_calls):
            logger.info("[trace] No tool calls detected, forcing retrieval...")
            # Create a forced tool call to the first retriever
            if self.retriever_tools:
                tool_name = self.retriever_tools[0].name
                logger.info(f"[trace] Forcing tool call to: {tool_name}")
                # Manually create tool call
                response.tool_calls = [{
                    "name": tool_name,
                    "args": {"query": augmented_messages[-1]["content"] if augmented_messages else "retrieve documents"},
                    "id": "forced_call"
                }]
        logger.info(f"[trace] Final response has tool_calls: {bool(hasattr(response, 'tool_calls') and response.tool_calls)}")
        return {"messages": [response]}
    def _grade_documents(
        self,
        state: MessagesState
    ) -> Literal["generate_answer", "rewrite_question"]:
        """
        Determine whether the retrieved documents are relevant to the question.

        Args:
            state: Current state containing messages

        Returns:
            str: Next node to execute ("generate_answer" or "rewrite_question")
        """
        logger.debug("Grading retrieved documents")
        question = state["messages"][0].content
        # Reuse the same context assembly as in _generate_answer
        def _extract_tool_context(messages: List[Any]) -> str:
            texts: List[str] = []
            for msg in messages:
                role = None
                if hasattr(msg, 'role'):
                    role = msg.role
                elif hasattr(msg, 'type'):
                    role = msg.type
                elif isinstance(msg, dict):
                    role = msg.get('role', None)
                is_tool = (role == 'tool') or (getattr(msg, '__class__', type('X',(object,),{})).__name__ == 'ToolMessage')
                if not is_tool:
                    continue
                content = None
                if hasattr(msg, 'content'):
                    content = msg.content
                elif isinstance(msg, dict):
                    content = msg.get('content', None)
                if isinstance(content, str):
                    texts.append(content)
                elif isinstance(content, list):
                    for item in content:
                        if hasattr(item, 'page_content'):
                            texts.append(str(item.page_content))
                        elif isinstance(item, dict):
                            if 'page_content' in item:
                                texts.append(str(item['page_content']))
                            elif 'content' in item:
                                texts.append(str(item['content']))
                            else:
                                texts.append(str(item))
                        else:
                            texts.append(str(item))
                elif isinstance(content, dict):
                    if 'page_content' in content:
                        texts.append(str(content['page_content']))
                    elif 'content' in content:
                        texts.append(str(content['content']))
                    else:
                        texts.append(str(content))

            merged = "\n\n".join(texts).strip()
            logger.info(f"[trace] grade_context_length={len(merged)}")
            return merged

        context = _extract_tool_context(state["messages"]) or state["messages"][-1].content
        grade_prompt = (
            "You are a grader assessing relevance of a retrieved document to a user question. \n "
            "Here is the retrieved document: \n\n {context} \n\n"
            "Here is the user question: {question} \n"
            "If the document contains keyword(s) or semantic meaning related to the user question, grade it as relevant. \n"
            "Give a binary score 'yes' or 'no' score to indicate whether the document is relevant to the question."
        )
        prompt = grade_prompt.format(question=question, context=context)
        response = (
            self.grader_model
            .with_structured_output(GradeDocuments)
            .invoke([{"role": "user", "content": prompt}])
        )
        score = response.binary_score
        logger.info(f"[trace] grade_score={score}")
        if score == "yes":
            return "generate_answer"
        else:
            return "rewrite_question"

    def _rewrite_question(self, state: MessagesState) -> Dict:
        """
        Rewrite the original user question to improve retrieval.

        Args:
            state: Current state containing messages

        Returns:
            Dict: Updated state with rewritten question
        """
        logger.debug("Rewriting question")
        last_human_message = None
        for message in reversed(state["messages"]):
            if isinstance(message, HumanMessage):
                last_human_message = message
                break
        question = last_human_message.content
        rewrite_prompt = (
            "Look at the input and try to reason about the underlying semantic intent / meaning.\n"
            "Here is the initial question:"
            "\n ------- \n"
            "{question}"
            "\n ------- \n"
            "Formulate an improved question then response in Vietnamese:"
        )
        prompt = rewrite_prompt.format(question=question)
        response = self.response_model.invoke([{"role": "user", "content": prompt}])
        logger.debug(f"Original question: {question}")
        logger.debug(f"Rewritten question: {response.content}")
        return {"messages": [{"role": "user", "content": response.content}]}

    def _generate_answer(self, state: MessagesState) -> Dict:
        """
        Generate an answer based on the retrieved documents.
        Always use MCQ mode since this project is for multiple-choice questions.

        Args:
            state: Current state containing messages

        Returns:
            Dict: Updated state with generated answer
        """
        logger.debug("Generating answer")
        logger.info("[trace] _generate_answer called")
        question = state["messages"][0].content
        # Assemble context from ToolMessages (robust against different formats)
        def _extract_tool_context(messages: List[Any]) -> str:
            texts: List[str] = []
            num_docs = 0
            num_tools = 0
            pre_merge_total_len = 0
            meta_summaries: List[str] = []

            def _try_append(item: Any):
                nonlocal num_docs, pre_merge_total_len, meta_summaries
                # LangChain Document-like object
                if hasattr(item, "page_content"):
                    txt = str(getattr(item, "page_content", ""))
                    texts.append(txt)
                    pre_merge_total_len += len(txt)
                    num_docs += 1
                    # metadata
                    md = getattr(item, "metadata", {}) or {}
                    srcn = md.get("source_normalized", md.get("source", ""))
                    pno = md.get("page_no", md.get("page", md.get("page_number", "")))
                    if srcn or pno != "":
                        meta_summaries.append(f"{srcn}:{pno}")
                    return True
                # Dict-like document
                if isinstance(item, dict):
                    if "page_content" in item:
                        txt = str(item.get("page_content", ""))
                        texts.append(txt)
                        pre_merge_total_len += len(txt)
                        num_docs += 1
                        md = item.get("metadata", {}) or {}
                        srcn = md.get("source_normalized", md.get("source", ""))
                        pno = md.get("page_no", md.get("page", md.get("page_number", "")))
                        if srcn or pno != "":
                            meta_summaries.append(f"{srcn}:{pno}")
                        return True
                    if "content" in item:
                        txt = str(item.get("content", ""))
                        texts.append(txt)
                        pre_merge_total_len += len(txt)
                        num_docs += 1
                        md = item.get("metadata", {}) or {}
                        srcn = md.get("source_normalized", md.get("source", ""))
                        pno = md.get("page_no", md.get("page", md.get("page_number", "")))
                        if srcn or pno != "":
                            meta_summaries.append(f"{srcn}:{pno}")
                        return True
                # Fallback: just stringify
                s = str(item)
                texts.append(s)
                pre_merge_total_len += len(s)
                return False

            for msg in messages:
                # role detection
                role = None
                if hasattr(msg, "role"):
                    role = msg.role
                elif hasattr(msg, "type"):
                    role = msg.type
                elif isinstance(msg, dict):
                    role = msg.get("role", None)

                is_tool = (role == "tool") or (getattr(msg, "__class__", type("X",(object,),{})).__name__ == "ToolMessage")
                if not is_tool:
                    continue
                num_tools += 1

                # content extraction
                content = None
                if hasattr(msg, "content"):
                    content = msg.content
                elif isinstance(msg, dict):
                    content = msg.get("content", None)

                if isinstance(content, str):
                    # Thử parse JSON để trích xuất Document nếu tool trả về JSON dưới dạng chuỗi
                    parsed = None
                    try:
                        stripped = content.strip()
                        if (stripped.startswith("{") and stripped.endswith("}")) or (stripped.startswith("[") and stripped.endswith("]")):
                            parsed = json.loads(stripped)
                    except Exception:
                        parsed = None
                    if parsed is not None:
                        # parsed có thể là 1 doc (dict) hoặc danh sách docs
                        if isinstance(parsed, list):
                            for item in parsed:
                                _try_append(item)
                        elif isinstance(parsed, dict):
                            # Một số tool trả {"documents": [...]} hay {"result": [...]}
                            if "documents" in parsed and isinstance(parsed["documents"], list):
                                for item in parsed["documents"]:
                                    _try_append(item)
                            elif "result" in parsed and isinstance(parsed["result"], list):
                                for item in parsed["result"]:
                                    _try_append(item)
                            else:
                                _try_append(parsed)
                    else:
                        # Không phải JSON hợp lệ, coi như text thuần
                        texts.append(content)
                        pre_merge_total_len += len(content)
                elif isinstance(content, list):
                    for item in content:
                        _try_append(item)
                elif isinstance(content, dict):
                    _try_append(content)

                # Extra fallbacks from additional_kwargs/response_metadata
                try:
                    addkw = getattr(msg, "additional_kwargs", None)
                    if isinstance(addkw, dict):
                        for k in ["output", "content", "result", "messages"]:
                            if k in addkw and addkw[k]:
                                # can be complex; just stringify
                                s = str(addkw[k])
                                texts.append(s)
                                pre_merge_total_len += len(s)
                except Exception:
                    pass
                try:
                    resp_meta = getattr(msg, "response_metadata", None)
                    if isinstance(resp_meta, dict):
                        for k in ["output", "content", "result"]:
                            if k in resp_meta and resp_meta[k]:
                                s = str(resp_meta[k])
                                texts.append(s)
                                pre_merge_total_len += len(s)
                except Exception:
                    pass

            merged = "\n\n".join(texts).strip()
            # Logging chi tiết theo yêu cầu
            logger.info(f"[trace] retrieved_docs_count={num_docs}")
            if meta_summaries:
                # In ra tối đa 10 mục để gọn log
                short_list = ", ".join(meta_summaries[:10])
                more = "" if len(meta_summaries) <= 10 else f" (+{len(meta_summaries)-10} more)"
                logger.info(f"[trace] retrieved_docs_meta={short_list}{more}")
            else:
                logger.info(f"[trace] retrieved_docs_meta=[]")
            logger.info(f"[trace] pre_merge_total_length={pre_merge_total_len}")
            logger.info(f"[trace] tool_messages_seen={num_tools}")
            logger.info(f"[trace] context_merged_length={len(merged)}")
            return merged

        context = _extract_tool_context(state["messages"]) or state["messages"][-1].content

        logger.info(f"[trace] question={question[:100]}...")
        logger.info(f"[trace] context_length={len(context)}")

        # Extract multiple-choice options from the original user question
        options_detected = {}
        try:
            # Look for options in the first user message (original question)
            first_user = None
            messages = state["messages"]
            logger.info(f"[trace] _generate_answer messages count: {len(messages)}")

            for i, m in enumerate(messages):
                # Try different ways to get role
                role = None
                if hasattr(m, 'role'):
                    role = m.role
                elif hasattr(m, 'type'):
                    role = m.type
                elif isinstance(m, dict):
                    role = m.get('role', 'unknown')

                if role in ["user", "human"]:
                    first_user = m
                    break

            if first_user:
                # Try different ways to get content
                content = None
                if hasattr(first_user, 'content'):
                    content = first_user.content
                elif isinstance(first_user, dict):
                    content = first_user.get('content', '')

                if content and isinstance(content, str):
                    logger.info(f"[trace] first_user.content={content[:200]}...")
                    for key in ["A", "B", "C", "D"]:
                        mopt = re.search(rf"\b{key}\s*[:\-]\s*(.+)", content, flags=re.IGNORECASE)
                        if mopt:
                            options_detected[key] = mopt.group(1).strip()
                            logger.info(f"[trace] found option {key}: {mopt.group(1).strip()[:50]}...")

            logger.info(f"[trace] mcq_options_detected={list(options_detected.keys())}")
        except Exception as e:
            logger.warning(f"[trace] Failed to detect MCQ options: {e}")

        # Always use MCQ mode for this project - no need to detect, just use what we found
        if not options_detected:
            # Fallback: create dummy options if none detected
            options_detected = {"A": "Option A", "B": "Option B", "C": "Option C", "D": "Option D"}
            logger.info("[trace] No options detected, using dummy options for MCQ mode")

        options_text = "\n".join([f"{k}) {v}" for k, v in options_detected.items()])
        mcq_prompt = (
            "Bạn là trợ lý trả lời trắc nghiệm. Hãy dùng ngữ cảnh để đánh giá từng lựa chọn và liệt kê tất cả đáp án đúng.\n"
            "Yêu cầu: thinking chi tiết quá trình suy nghĩ; rationale ngắn gọn bằng tiếng Việt; final_answer chỉ là các chữ cái (A,B,...) không thêm ký tự khác.\n"
            f"Câu hỏi: {question}\n"
            f"Lựa chọn:\n{options_text}\n"
            f"Ngữ cảnh:\n{context}"
        )
        try:
            structured = self.response_model.with_structured_output(MCQAnswer).invoke([{"role": "user", "content": mcq_prompt}])
            content = f"Thinking: {structured.thinking}\nRationale: {structured.rationale}\nFinal Answer: {structured.final_answer}"
            logger.info("[trace] structured_output=success (MCQ)")
            return {"messages": [{"role": "assistant", "content": content}]}
        except Exception as e:
            logger.info(f"[trace] structured_output=fallback (MCQ): {e}")
            fallback_prompt = (
                "Bạn là trợ lý trả lời trắc nghiệm. Hãy dùng ngữ cảnh để đánh giá từng lựa chọn và liệt kê tất cả đáp án đúng.\n"
                "Hãy trả lời theo đúng định dạng: Thinking: ...\nRationale: ...\nFinal Answer: A,B\n"
                f"Câu hỏi: {question}\n"
                f"Lựa chọn:\n{options_text}\n"
                f"Ngữ cảnh:\n{context}"
            )
            response = self.response_model.invoke([{"role": "user", "content": fallback_prompt}])
            return {"messages": [response]}

    def update_thread_id(self, new_thread_id: Optional[str] = None) -> str:
        """
        Update the thread_id for the conversation.

        Args:
            new_thread_id: New thread ID to use. If None, generates a new unique thread_id.

        Returns:
            str: The updated thread_id
        """
        if new_thread_id is None:
            self.thread_id = generate_thread_id()
        else:
            self.thread_id = new_thread_id

        logger.info(f"Thread ID updated to: {self.thread_id}")
        return self.thread_id

    def get_config(self) -> Dict[str, Any]:
        """
        Get the configuration dictionary for the agent.

        Returns:
            Dict[str, Any]: Configuration dictionary with thread_id
        """
        return {"configurable": {"thread_id": self.thread_id}}

    def run_mcq(self, question: str, options: Dict[str, str]) -> str:
        """
        Run the agent on a multiple-choice question with options A/B/C/D.
        The question string may also contain a document hint (e.g., "dựa vào tài liệu Public001").
        Options should be a dict like {"A": "...", "B": "...", "C": "...", "D": "..."}.
        """
        logger.info(f"[trace] run_mcq called with question: {question[:100]}...")
        logger.info(f"[trace] run_mcq options: {list(options.keys())}")

        # Build a single user message that includes question and labeled options
        opts_text = []
        for key in ["A", "B", "C", "D"]:
            if key in options and options[key]:
                opts_text.append(f"{key}: {options[key]}")
        options_block = "\n".join(opts_text)
        content = f"{question}\n{options_block}" if options_block else question

        logger.info(f"[trace] run_mcq content: {content[:200]}...")

        # Reset thread per question to avoid cross-row context leakage
        self.update_thread_id()
        msg = {"messages": [{"role": "user", "content": content}]}
        config = self.get_config()

        logger.info(f"[trace] run_mcq invoking graph...")
        result = self.graph.invoke(msg, config)
        final_message = result["messages"][-1]

        logger.info(f"[trace] run_mcq result: {final_message.content[:200]}...")
        return final_message.content

    def run_mcq_csv(self, csv_path: Union[str, os.PathLike]) -> List[Dict[str, Any]]:
        """
        Batch-run MCQ questions from a CSV file with columns: Question, A, B, C, D.
        Returns a list of dicts: {"question": ..., "A": ..., ..., "response": ...}
        """
        rows: List[Dict[str, Any]] = []
        with open(csv_path, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                q = row.get("Question", "")
                options = {k: row.get(k, "") for k in ["A", "B", "C", "D"]}
                try:
                    # Reset thread per row
                    self.update_thread_id()
                    response = self.run_mcq(q, options)
                except Exception as e:
                    response = f"Error: {e}"
                rows.append({"question": q, **options, "response": response})
        return rows

    def run(self, query: str) -> str:
        """
        Run the agentic RAG system with a query.

        Args:
            query: User query

        Returns:
            str: Generated response
        """
        logger.info(f"Running agentic RAG with query: {query}")
        # Create initial state
        message = {"messages": [{"role": "user", "content": query}]}
        # Run the graph
        config = self.get_config()
        result = self.graph.invoke(message, config)
        # Extract the final response
        final_message = result["messages"][-1]
        response = final_message.content
        logger.info("Agentic RAG execution completed")
        return response


"""
Main script for MCQ RAG prediction using AI Agent with Milvus retrieval.

This script demonstrates the retrieval and AI agent-based approach for answering
multiple-choice questions by combining:
1. Milvus vector store for document retrieval
2. AgenticRAG for intelligent question answering
3. Response parsing to extract thinking, rationale, and final answers

Usage:
    python main2.py
"""

import os
import sys
import re
import logging
from pathlib import Path
from pprint import pprint

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent))

from src.milvus_store import MilvusStore
from src.config import ConfigLoader
from src.agent import AgenticRAG


def initialize_components():
    """
    Initialize configuration, vector store, and AI agent.

    Returns:
        tuple: (agent, config) - AgenticRAG instance and ConfigLoader instance
    """
    logger.info("Initializing components...")

    # Load configuration
    config = ConfigLoader("config.yaml")

    # Set collection name for retrieval
    config.set("database", "collection_name", "doc_2_db")

    # Get configuration parameters
    uri = config.get("database", "uri", default="http://localhost:19530")
    db_name = config.get("database", "name", default="gil")
    collection_name = config.get("database", "collection_name", default="multimodal_rag")
    embed_model = config.get("model", "embeddings",
                            default="sentence-transformers/paraphrase-multilingual-mpnet-base-v2")
    k = config.get("retrieval", "k", default=3)
    ranker_weights = config.get("retrieval", "weights", default=[0.6, 0.4])

    logger.info(f"Configuration loaded:")
    logger.info(f"  URI: {uri}")
    logger.info(f"  Database: {db_name}")
    logger.info(f"  Collection: {collection_name}")
    logger.info(f"  Retrieval K: {k}")

    # Initialize Milvus vector store
    logger.info("Initializing Milvus vector store...")
    milvus_store = MilvusStore(
        uri=uri,
        db_name=db_name,
        collection_name=collection_name,
        embed_model=embed_model,
        drop_old=False
    )

    # Create vector store configuration
    vector_store_config = {
        "store": milvus_store,
        "name": "retrieve_documents_on_docling",
        "description": "Search and retrieve information from the document collection on a topic of docling",
        "k": k,
        "ranker_weights": ranker_weights
    }

    # Initialize AI Agent
    logger.info("Initializing AgenticRAG...")
    agent = AgenticRAG(vector_stores=[vector_store_config])

    logger.info("Components initialized successfully!")
    return agent, config


def parse_agent_response(response: str) -> dict:
    """
    Parse the AI agent response to extract thinking, rationale, and final answer.

    Args:
        response: The full response from the AI agent

    Returns:
        dict: Dictionary containing 'thinking', 'rationale', and 'final_answer'
    """
    # Extract thinking content from <think>...</think> tags
    thinking_match = re.search(r"<think>(.*?)</think>", response, re.DOTALL)
    thinking_text = thinking_match.group(1).strip() if thinking_match else ""

    # Remove thinking section from response
    remainder = re.sub(r"<think>.*?</think>", "", response, flags=re.DOTALL).strip()

    # Extract rationale
    rationale_match = re.search(r"Rationale:(.*?)(?:Final Answer:|$)", remainder, re.DOTALL)
    rationale_text = rationale_match.group(1).strip() if rationale_match else ""

    # Extract final answer
    final_match = re.search(r"Final Answer:\s*(.*)", remainder)
    final_answer = final_match.group(1).strip() if final_match else ""

    return {
        "thinking": thinking_text,
        "rationale": rationale_text,
        "final_answer": final_answer
    }


def print_result(result: dict, verbose: bool = True):
    """
    Print a formatted result from the agent.

    Args:
        result: Dictionary containing question and response
        verbose: If True, print thinking and rationale; if False, only final answer
    """
    question = result.get("question", "")
    response = result.get("response", "")

    parsed = parse_agent_response(response)

    print(f"\n{'='*80}")
    print(f"❓ Question: {question}")
    print(f"{'='*80}")

    if verbose:
        if parsed["thinking"]:
            print("\n🧠 Thinking Process:")
            print("-" * 40)
            pprint(parsed["thinking"])

        if parsed["rationale"]:
            print("\n📚 Rationale:")
            print("-" * 40)
            pprint(parsed["rationale"])

    print("\n💬 Final Answer:")
    print("-" * 40)
    print(parsed["final_answer"])
    print(f"{'='*80}\n")


def process_csv_file(agent: AgenticRAG, csv_path: str, output_verbose: bool = True) -> list:
    """
    Process a CSV file with questions and generate AI agent responses.

    Args:
        agent: AgenticRAG instance
        csv_path: Path to CSV file containing questions
        output_verbose: If True, print detailed responses; if False, only final answers

    Returns:
        list: List of results with questions and responses
    """
    logger.info(f"Processing CSV file: {csv_path}")

    if not os.path.exists(csv_path):
        logger.error(f"CSV file not found: {csv_path}")
        return []

    # Run agent on CSV
    results = agent.run_mcq_csv(csv_path)

    logger.info(f"Processing complete! Total results: {len(results)}")

    # Print results
    for i, result in enumerate(results, 1):
        logger.info(f"Result {i}/{len(results)}")
        print_result(result, verbose=output_verbose)

    return results


def save_results_to_file(results: list, output_path: str = "results.txt"):
    """
    Save results to a text file.

    Args:
        results: List of results from agent
        output_path: Path to output file
    """
    logger.info(f"Saving results to {output_path}...")

    with open(output_path, 'w', encoding='utf-8') as f:
        for i, result in enumerate(results, 1):
            question = result.get("question", "")
            response = result.get("response", "")

            parsed = parse_agent_response(response)

            f.write(f"\n{'='*80}\n")
            f.write(f"Question {i}: {question}\n")
            f.write(f"{'='*80}\n")

            if parsed["thinking"]:
                f.write(f"\nThinking Process:\n{parsed['thinking']}\n")

            if parsed["rationale"]:
                f.write(f"\nRationale:\n{parsed['rationale']}\n")

            f.write(f"\nFinal Answer:\n{parsed['final_answer']}\n")
            f.write(f"\n{'='*80}\n")

    logger.info(f"Results saved to {output_path}")


def main():
    """Main execution function."""
    try:
        # Initialize components
        agent, config = initialize_components()

        # Process test CSV
        csv_path = "test.csv"
        results = process_csv_file(agent, csv_path, output_verbose=True)

        # Save results to file
        save_results_to_file(results, output_path="agent_results.txt")

        logger.info("Processing complete!")
        return results

    except Exception as e:
        logger.error(f"Error during processing: {str(e)}", exc_info=True)
        raise


if __name__ == "__main__":
    results = main()
