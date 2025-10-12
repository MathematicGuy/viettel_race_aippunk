import os
import pandas as pd
from pathlib import Path
import torch
import clip
from sentence_transformers import SentenceTransformer

from .pipeline import create_hybrid_pipeline
from .image_encoder import MultimodalImageEncoder
from .llm_utils import load_llm
from .retrieval_qa import get_relevant_documents, prompt, MCQInput
from .milvus_store import MilvusHybridStore
from .search_engine import HybridSearchEngine

# Device
device = "cuda" if torch.cuda.is_available() else "cpu"

# ===== MODEL INITIALIZATION =====
# Text embedding model
text_model = SentenceTransformer('sentence-transformers/paraphrase-multilingual-mpnet-base-v2').to(device)

# Multimodal embedding model (CLIP cho text-image joint embedding)
clip_model, clip_preprocess = clip.load("ViT-B/32", device=device)
clip_model.eval()

# Image encoder instance
image_encoder = MultimodalImageEncoder(clip_model, clip_preprocess)

# LLM
llm = load_llm()

def main():
    # Configuration
    IMAGE_BASE_DIR = 'private_test_output/images'
    MILVUS_URI = "https://in03-7b3b56e59d62e9d.serverless.aws-eu-central-1.cloud.zilliz.com"
    MILVUS_TOKEN = "30cff684b802d87f26e0c7ea80e43c759237808981ac1563ae400b00316ff84be4261492ee91b9f55ec6ad8a25b7be9b483fc957"

    # Get file names
    PATH = "private_test_output/"
    file_names = [f for f in os.listdir(PATH) if f.lower().endswith(".pdf")]
    file_names = [f[:-4] for f in file_names]

    for file_name in file_names:
        MARKDOWN_DIR = f'IMAGE_BASE_DIR\\{file_name}'
        process_docs, search_engine = create_hybrid_pipeline(
            MARKDOWN_DIR, IMAGE_BASE_DIR, MILVUS_URI, MILVUS_TOKEN, text_model, image_encoder
        )

        # Xử lý documents
        markdown_files = list(Path(MARKDOWN_DIR).glob("*.md"))
        print(markdown_files)
        entities, search_engine = process_docs(markdown_files)

        # Test search for this file
        print(f"\n{'='*60}")
        print(f"TEST HYBRID SEARCH for {file_name}")
        print(f"{'='*60}")

        # Text search
        text_results = search_engine.hybrid_search(
            query_text="Trong mô hình nhà thông minh, IoT chủ yếu đóng vai trò gì?",
            limit=5
        )
        print(f"Text search results: {len(text_results)}")
        for i, result in enumerate(text_results[:3]):
            print(f"  {i+1}. Score: {result['distance']:.4f}")
            print(f"     Content: {result['entity']['content']}...")
            print(f"     Type: {result['entity']['metadata']['entity_type']}")

    # After processing all, load questions and answer
    csv_path = "question.csv"
    df = pd.read_csv(csv_path)

    # Extract each row into a list of MCQInput objects
    mcq_list = []
    for _, row in df.iterrows():
        mcq = MCQInput(
            question=str(row['Question']) if pd.notna(row['Question']) else "",
            option_a=str(row['A']) if pd.notna(row['A']) else "",
            option_b=str(row['B']) if pd.notna(row['B']) else "",
            option_c=str(row['C']) if pd.notna(row['C']) else "",
            option_d=str(row['D']) if pd.notna(row['D']) else ""
        )
        mcq_list.append(mcq)

    print(f"Total questions loaded: {len(mcq_list)}")

    answers = []
    # Process first 5 for demo
    for i, mcq in enumerate(mcq_list):
        print(f"Processing question {i+1}: {mcq.question}")
        # Retrieval
        retrieved_context = get_relevant_documents(search_engine, mcq.question)
        context = "\n".join([doc.page_content for doc in retrieved_context])
        response = llm.invoke(prompt.format(context=context, **mcq.model_dump()))
        # Extract answer
        import re
        pattern = r'\{"answer":\s*"([A-D, ]+)"\}'
        match = re.search(pattern, response)

        if match:
            answer = match.group(1)
            print(f"Answer: {answer}")
            answers.append(answer)
        else:
            print("No match found")

if __name__ == "__main__":
    main()