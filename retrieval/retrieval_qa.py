import base64
from io import BytesIO
from langchain.schema import Document
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from PIL import Image
from pydantic import BaseModel


class MCQAnswer(BaseModel):
    answer: str


class MCQInput(BaseModel):
    question: str
    option_a: str
    option_b: str
    option_c: str
    option_d: str


def get_relevant_documents(search_engine, query: str) -> list[Document]:
    results = search_engine.hybrid_search(query, limit=5)
    docs = []
    for result in results:
        content = result['entity']['content']
        if result['entity']['image_path']:
            # Đọc và mã hóa hình ảnh thành base64 để nhúng vào context
            try:
                image_path = result['entity']['image_path']
                with Image.open(image_path) as img:
                    buffered = BytesIO()
                    img.save(buffered, format="PNG")
                    img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")
                    content += f" <image>{img_str}</image>"  # Định dạng phù hợp với Qwen-VL
            except Exception as e:
                content += f" [Failed to load image: {str(e)}]"

        docs.append(Document(page_content=content, metadata=result['entity']['metadata']))

    return docs


# --- Define Prompt ---
parser = PydanticOutputParser(pydantic_object=MCQAnswer)

prompt = PromptTemplate(
    template=(
        "You are a strict assistant. "
        "Use the given context to answer the multiple-choice question below.\n\n"
        "Return only a JSON object in this format:\n"
        "{{\"answer\": \"<A|B|C|D>\"}}\n\n"
        "Context: {context}\n"
        "Question: {question}\n"
        "A. {option_a}\nB. {option_b}\nC. {option_c}\nD. {option_d}\n\n"
        "Return the correct answer as letter (i.e. A, B, C, D). If there are multiple correct answer then seperate them by a comma e.g. 'A, B'"
        "Do not add any extra text.\n"
    ),
    input_variables=["context", "question", "option_a", "option_b", "option_c", "option_d"],
    partial_variables={"format_instructions": parser.get_format_instructions()},
)
