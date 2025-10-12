import os
import shutil
from pathlib import Path

def reorganize_directory(root_dir):
    """
    Reorganize directories by moving clean_*.md to main.md and images folder up one level,
    then remove the auto directory.
    """
    root_path = Path(root_dir)

    # Iterate through all PublicXXX directories
    for public_dir in sorted(root_path.glob('Public*')):
        if not public_dir.is_dir():
            continue

        auto_dir = public_dir / 'auto'
        if not auto_dir.exists():
            print(f"Skipping {public_dir}: no 'auto' directory found")
            continue

        print(f"Processing {public_dir}")

        # Find and process clean_*.md file
        for clean_file in auto_dir.glob('clean_*.md'):
            # Rename to main.md and move to parent directory
            new_path = public_dir / 'main.md'
            shutil.move(str(clean_file), str(new_path))
            print(f"  Moved {clean_file.name} to {new_path}")

        # Move images directory if it exists
        images_dir = auto_dir / 'images'
        if images_dir.exists() and images_dir.is_dir():
            new_images_dir = public_dir / 'images'
            if new_images_dir.exists():
                shutil.rmtree(str(new_images_dir))
            shutil.move(str(images_dir), str(public_dir))
            print(f"  Moved images/ to {public_dir}/")

        # Remove the auto directory
        try:
            shutil.rmtree(str(auto_dir))
            print(f"  Removed {auto_dir}/")
        except Exception as e:
            print(f"  Error removing {auto_dir}: {e}")


if __name__ == "__main__":
    # Get the directory where this script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    out_dir = os.path.join(script_dir, 'out')

    if os.path.exists(out_dir):
        print(f"Starting reorganization of {out_dir}")
        reorganize_directory(out_dir)
        print("Reorganization completed!")
    else:
        print(f"Error: Directory not found: {out_dir}")