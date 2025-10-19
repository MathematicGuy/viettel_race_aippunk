import os
import shutil
import re
from pathlib import Path

print('BEGIN cleaning markdown')
def clean_markdown(root_dir):
    """
    Clean each markdown file by replace raw heading with markdown heading format
    e.g # 1. -> #, 1.1 -> ##, 1.1.1 -> ### (replace by the dots)
    """
    root_path = Path(root_dir)

    # Iterate through all PublicXXX directories
    for public_dir in sorted(root_path.glob('Public*')):
        if not public_dir.is_dir():
            continue

        main_file = public_dir / 'main.md'
        if not main_file.exists():
            print(f"Skipping {public_dir}: no 'main.md' file found")
            continue

        print(f"Processing {public_dir}")

        # Read the markdown file
        with open(main_file, 'r', encoding='utf-8') as f:
            content = f.read()


        processed_text = process_markdown_comments(content)
        # print(processed_text)

        # Function to convert header notation to markdown headers
        def convert_header(match):
            # Extract the number pattern (e.g., "1", "1.1", "1.2.3")
            header_text = match.group(1)
            # Extract the title (everything after the number series)
            title_text = match.group(2)
            # Count the number of segments (numbers separated by dots)
            # e.g., "1" -> 1 segment, "1.1" -> 2 segments, "1.2.1" -> 3 segments
            # Remove trailing dot if present and count segments
            clean_header = header_text.rstrip('.')
            segments = len(clean_header.split('.'))
            heading_level = segments

            # Return markdown heading with appropriate number of # symbols (number series removed)
            return '#' * heading_level + ' ' + title_text

        # Replace headers like "# 1.", "# 1.1", "# 1.2.1", etc.
        # Pattern: # followed by optional space, then digits and dots, then optional period and space, then capture the title
        cleaned_content = re.sub(r'^# +(\d+(?:\.\d+)*\.?)\s+(.+)$', convert_header, processed_text, flags=re.MULTILINE)

        # Write the cleaned content back to the file
        with open(f'{public_dir}/main.md', 'w', encoding='utf-8') as f:
            f.write(cleaned_content)

        print(f"✓ Cleaned {public_dir}")


def process_markdown_comments(text):
    """
    Adds an underscore to lines that start with '#' but are likely code comments,
    not Markdown headers.

    Args:
        text: A string containing the Markdown content.

    Returns:
        A string with the corrected content.
    """
    processed_lines = []
    lines = text.split('\n')

    for line in lines:
        # We only care about non-empty lines that start with '#'
        stripped_line = line.strip()
        if not stripped_line.startswith('#'):
            processed_lines.append(line)
            continue

        # --- HEURISTIC LOGIC ---
        # A line is considered a code comment if:
        # 1. It contains a Python function definition keyword.
        is_function_def = 'def ' in stripped_line

        # 2. There is no space after the hashes (e.g., "#comment" vs "# header").
        #    This regex checks for one or more '#' followed by a non-space character.
        no_space_after_hash = re.match(r'^#+[^#\s]', stripped_line)

        if is_function_def or no_space_after_hash:
            # This is a code comment, so add an underscore to the original line
            processed_lines.append('_' + line + '_')
        else:
            # This is a legitimate Markdown header, leave it as is
            processed_lines.append(line)

    return '\n'.join(processed_lines)


if __name__ == "__main__":
    # Get the directory where this script is located
    # PATH = 'private-test-output'
    PATH = 'Public_test_input'
    out_dir = os.path.join(PATH)
    print(out_dir)

    if os.path.exists(out_dir):
        print(f"Starting reorganization of {out_dir}")
        clean_markdown(out_dir)
        print("Reorganization completed!")
    else:
        print(f"Error: Directory not found: {out_dir}")