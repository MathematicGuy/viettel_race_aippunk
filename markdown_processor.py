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