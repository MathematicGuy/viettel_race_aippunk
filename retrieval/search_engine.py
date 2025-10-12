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
