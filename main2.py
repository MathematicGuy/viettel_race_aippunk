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
