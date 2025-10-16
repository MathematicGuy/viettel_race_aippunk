import re

def process_markdown_python_comments(text: str) -> str:
    """
    Analyzes markdown text to identify and format Python code comments.

    Args:
        text: The input string containing mixed markdown and Python code.

    Returns:
        The processed string with Python comments formatted.
    """
    lines = text.split('\n')
    processed_lines = []

    in_code_block = False
    in_docstring = False

    for line in lines:
        stripped = line.strip()

        # --- State Management: Determine if we are in a code block ---

        # Heuristic to exit a code block: A major header or an image tag.
        if stripped.startswith('![](') or re.match(r'^#\s', stripped):
            in_code_block = False
            in_docstring = False # Reset docstring state as well

        # Heuristic to enter a code block: A function or import statement.
        if stripped.startswith('def ') or stripped.startswith('import '):
            in_code_block = True

        # --- Line Processing ---

        # Special case: A comment and `def` on the same line, which also starts a code block.
        # Example: "# Cách1 def add_boder(...)" -> "_# Cách1_ def add_boder(...)"
        match = re.match(r'^(#.*?)\s+(def\s+.*)', stripped)
        if match:
            in_code_block = True  # This line confirms we are in a code block
            indent = line[:line.find('#')]
            processed_lines.append(f"{indent}_{match.group(1)}_ {match.group(2)}")
            continue

        if in_code_block:
            # Rule for docstrings (""")
            if '"""' in stripped:
                processed_lines.append(f"_{line}_")
                # Toggle state if it's a multi-line docstring delimiter
                if stripped.count('"""') == 1:
                    in_docstring = not in_docstring
                continue

            # Rule for lines inside a multi-line docstring
            if in_docstring:
                processed_lines.append(f"_{line}_")
                continue

            # Rule for regular full-line comments (#)
            if stripped.startswith('#'):
                processed_lines.append(f"_{line}_")
                continue

        # If no rule was met, append the line as is.
        processed_lines.append(line)

    return '\n'.join(processed_lines)



processed_text = process_markdown_python_comments(sample_text)
print(processed_text)