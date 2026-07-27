"""Run every numbered example in the 01_objects_syntax folder."""
from pathlib import Path
import runpy

current_file = Path(__file__).resolve()
for example in sorted(current_file.parent.glob("*.py")):
    if example.name == current_file.name:
        continue
    print("\n" + "=" * 80)
    print(f"Running {example.name}")
    print("=" * 80)
    try:
        runpy.run_path(str(example), run_name="__main__")
    except Exception as error:
        print(f"Example raised {type(error).__name__}: {error}")
