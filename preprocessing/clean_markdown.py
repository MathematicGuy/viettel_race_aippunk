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
        cleaned_content = re.sub(r'^# +(\d+(?:\.\d+)*\.?)\s+(.+)$', convert_header, content, flags=re.MULTILINE)

        # Write the cleaned content back to the file
        with open(f'{public_dir}/clean_main.md', 'w', encoding='utf-8') as f:
            f.write(cleaned_content)

        print(f"✓ Cleaned {public_dir}")



if __name__ == "__main__":
    # Get the directory where this script is located
    PATH = 'private-test-output'
    out_dir = os.path.join(PATH)
    print(out_dir)

    if os.path.exists(out_dir):
        print(f"Starting reorganization of {out_dir}")
        clean_markdown(out_dir)
        print("Reorganization completed!")
    else:
        print(f"Error: Directory not found: {out_dir}")