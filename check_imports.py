import sys
import os
from pathlib import Path

def run_import_test():
    """
    Tests importing the 'core' module and provides diagnostic information
    about the Python environment.
    """
    print("--- Python Import Test ---")

    # Get the expected project root (the 'app' directory)
    project_root = Path(__file__).parent.resolve()
    print(f"Expected Project Root: {project_root}")

    # --- 1. Current Working Directory ---
    cwd = os.getcwd()
    print(f"Current Working Directory: {cwd}")

    # --- 2. Python Search Path (sys.path) ---
    print("\nPython Search Path (sys.path):")
    for i, path in enumerate(sys.path):
        print(f"  {i}: {path}")

    # --- 3. Check if project root is in sys.path ---
    if str(project_root) not in sys.path and "" not in sys.path:
         print("\n[Warning] The project root is not explicitly in sys.path.")
         print("Adding it for this test...")
         sys.path.insert(0, str(project_root))
         print("Updated sys.path:")
         for i, path in enumerate(sys.path):
            print(f"  {i}: {path}")


    # --- 4. Attempting to import from 'core' ---
    print("\n--- Attempting to import from 'core' module ---")
    try:
        from core.pipeline import create_hybrid_pipeline
        print("\n✅ SUCCESS: Successfully imported 'create_hybrid_pipeline' from 'core.pipeline'.")
        print("The 'core' module seems to be structured correctly.")

    except ImportError as e:
        print(f"\n❌ FAILURE: Could not import from 'core'.")
        print(f"   Error: {e}")
        print("\n   Suggestion:")
        print(f"   This error usually means the project root ('{project_root.name}') is not in Python's path when you run your script.")
        print(f"   Ensure you are running your Python commands from the directory: {project_root}")

    except ModuleNotFoundError as e:
        print(f"\n❌ FAILURE: The 'core' module was not found.")
        print(f"   Error: {e}")
        print("\n   Suggestion:")
        print("   - Verify that the 'core' directory exists and is at the same level as this script.")
        print("   - Make sure the 'core' directory contains an '__init__.py' file to be recognized as a package.")


    print("\n--- Test Complete ---")

if __name__ == "__main__":
    run_import_test()
