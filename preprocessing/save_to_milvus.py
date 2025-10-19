# Get file names
import os, sys
from pathlib import Path
#? change current directory to root directory to run extract_data.sh
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))
print('Path:', project_root)

import torch
import clip
from sentence_transformers import SentenceTransformer
from core.hybrid_collection_pipeline import create_hybrid_pipeline
from models.image_encoder import MultimodalImageEncoder
# from storage.milvus_store import MilvusHybridStore
from retrieval.search_engine import HybridSearchEngine


print('BEGIN SAVE DATA TO LOCAL MILVUS DB')
# Configuration
PATH = 'Public_test_input'
OUTPUT_PATH = 'Public_test_output'
IMAGE_BASE_DIR = f'{OUTPUT_PATH}/images'
# MILVUS_URI = "https://in03-7b3b56e59d62e9d.serverless.aws-eu-central-1.cloud.zilliz.com"
# MILVUS_TOKEN = "30cff684b802d87f26e0c7ea80e43c759237808981ac1563ae400b00316ff84be4261492ee91b9f55ec6ad8a25b7be9b483fc957"
MILVUS_URI = "http://localhost:19530"
MILVUS_TOKEN = "root:Milvus"
# PATH = "private-test-output/"

# MODEL INITIALIZATION
device = "cuda" if torch.cuda.is_available() else "cpu"

# Multimodal embedding model (CLIP cho text-image joint embedding)
clip_model, clip_preprocess = clip.load("ViT-B/32", device=device)
clip_model.eval()

# Image encoder instance
image_encoder = MultimodalImageEncoder(clip_model, clip_preprocess)
# Text embedding model
text_model = SentenceTransformer('sentence-transformers/paraphrase-multilingual-mpnet-base-v2').to(device)


def save_to_milvus_pipeline(url, token, images_dir):
	file_names = [d for d in os.listdir(OUTPUT_PATH) if os.path.isdir(os.path.join(OUTPUT_PATH, d))]

	for file_name in file_names:
		MARKDOWN_DIR = os.path.join(OUTPUT_PATH, file_name)
		process_docs, search_engine = create_hybrid_pipeline(
			MARKDOWN_DIR, IMAGE_BASE_DIR, MILVUS_URI, MILVUS_TOKEN, text_model, image_encoder
		)

		# Xử lý documents
		markdown_files = list(Path(MARKDOWN_DIR).glob("*.md"))
		entities, search_engine = process_docs(markdown_files)  # ✓ Compatible!
		print(markdown_files)

		# Test search for this file
		print(f"\n{'='*60}")
		print(f"TEST HYBRID SEARCH for {file_name}")
		print(f"{'='*60}")


# Text search
if __name__ == '__main__':
	save_to_milvus_pipeline(MILVUS_URI, MILVUS_TOKEN, OUTPUT_PATH)

	#? Test Run After Save to MilvusDb
    # store = MilvusHybridStore(MILVUS_URI, MILVUS_TOKEN)
    # search_engine = HybridSearchEngine(store, text_model, image_encoder)

    # text_results = search_engine.hybrid_search(
    #     query_text="Trong mô hình nhà thông minh, IoT chủ yếu đóng vai trò gì?",
    #     limit=5
    # )
    # print(f"Text search results: {len(text_results)}")
    # for i, result in enumerate(text_results[:3]):
    #     print(f"  {i+1}. Score: {result['distance']:.4f}")
    #     print(f"     Content: {result['entity']['content']}...")
    #     print(f"     Type: {result['entity']['metadata']['entity_type']}")
