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