import os
import pandas as pd
from pathlib import Path
import torch
import clip
from sentence_transformers import SentenceTransformer

from core.hybrid_collection_pipeline import create_hybrid_pipeline
from models.image_encoder import MultimodalImageEncoder
from models.llm_utils import load_llm
from retrieval.retrieval_qa import get_relevant_documents, prompt, MCQInput
from storage.milvus_store import MilvusHybridStore
from retrieval.search_engine import HybridSearchEngine
from utils.write_answers import write_answers_to_file, write_extract_to_file
# set DEBUG logging for pymilvus
import logging

# Device
device = "cuda" if torch.cuda.is_available() else "cpu"
print(device)
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
    INPUT_PATH = "Public_test_input"
    OUTPUT_PATH = "Public_test_output"
    MILVUS_URI = "http://localhost:19530"
    MILVUS_TOKEN = "root:Milvus"
    # MILVUS_URI = "https://in03-7b3b56e59d62e9d.serverless.aws-eu-central-1.cloud.zilliz.com"
    # MILVUS_TOKEN = "30cff684b802d87f26e0c7ea80e43c759237808981ac1563ae400b00316ff84be4261492ee91b9f55ec6ad8a25b7be9b483fc957"

    logging.getLogger("pymilvus").setLevel(logging.DEBUG)
    store = MilvusHybridStore(MILVUS_URI, MILVUS_TOKEN)
    search_engine = HybridSearchEngine(store, text_model, image_encoder)

    # After processing all, load questions and answer
    csv_path = f"{INPUT_PATH}/question.csv"
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
            answers.append('C')
            print(response)

    write_extract_to_file(OUTPUT_PATH)
    write_answers_to_file(answers)


if __name__ == "__main__":
    main()