import os
from pathlib import Path

def combine_markdown_files(source_dir: str, output_file: str):
    """
    Combine all main.md files from PublicXXX subdirectories into a single markdown file.
    Processes folders in numerical order (Public001, Public002, etc.)

    Args:
        source_dir: Directory containing PublicXXX folders with main.md files
        output_file: Path to the output markdown file
    """
    source_path = Path(source_dir)
    output_path = Path(output_file)

    # Create output directory if it doesn't exist
    output_path.parent.mkdir(parents=True, exist_ok=True)

    # Start with the TASK EXTRACT header
    content = "### TASK EXTRACT\n\n"

    # Get all PublicXXX directories and sort them numerically
    public_dirs = sorted(
        [d for d in source_path.glob('Public*') if d.is_dir()],
        key=lambda x: int(x.name[6:]) if x.name[6:].isdigit() else float('inf')
    )

    for dir_path in public_dirs:
        main_file = dir_path / 'main.md'
        if not main_file.exists():
            continue

        dir_name = dir_path.name

        # Read the content of main.md
        try:
            with open(main_file, 'r', encoding='utf-8') as f:
                file_content = f.read().strip()

                # Add the file header and content
                content += f"# {dir_name}\n\n{file_content}\n\n"

        except Exception as e:
            print(f"Error processing {main_file}: {e}")

    # Write the combined content to the output file
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Successfully combined markdown files into {output_path}")

if __name__ == "__main__":
    # Define paths
    source_directory = "private-test-output"
    output_file = "private-test-output/answer.md"

    # Run the combination
    combine_markdown_files(source_directory, output_file)
