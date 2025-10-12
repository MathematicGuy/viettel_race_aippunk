from pathlib import Path
from typing import List
from .markdown_processor import MarkdownProcessor
from .entity_processors import TextEntityProcessor, ImageEntityProcessor
from .milvus_store import MilvusHybridStore
from .search_engine import HybridSearchEngine


def create_hybrid_pipeline(markdown_dir: str, image_base_dir: str,
                            uri: str, token: str, text_model, image_encoder):
    """Tạo pipeline hybrid search hoàn chỉnh"""

    # Initialize components
    processor = MarkdownProcessor(markdown_dir, image_base_dir)
    text_processor = TextEntityProcessor(text_model)
    image_processor = ImageEntityProcessor(image_encoder)
    store = MilvusHybridStore(uri, token)
    search_engine = HybridSearchEngine(store, text_model, image_encoder)

    # Tạo collection
    store.create_hybrid_collection()

    def process_documents(markdown_files: List[str]):
        """Xử lý documents thành entities"""
        all_entities = []

        for md_file in markdown_files:
            print(f"\n{'='*60}")
            print(f"Đang xử lý: {md_file}")
            print(f"{'='*60}")

            # Extract content
            content = processor.extract_content(Path(md_file))
            print(f"  - Text length: {len(content['text'])} ký tự")
            print(f"  - Số bảng: {len(content['tables'])}")
            print(f"  - Số hình ảnh: {len(content['images'])}")

            # Tạo text entities
            text_entities = text_processor.create_text_entities(content)
            print(f"  - Text entities: {len(text_entities)}")

            # Tạo image entities
            image_entities = image_processor.create_image_entities(content)
            print(f"  - Image entities: {len(image_entities)}")

            all_entities.extend(text_entities)
            all_entities.extend(image_entities)

                # Insert vào Milvus
        store.insert_entities(all_entities)

        print(f"\n✅ Pipeline hoàn tất! Tổng cộng {len(all_entities)} entities đã được xử lý.")
        return all_entities, search_engine

    return process_documents, search_engine