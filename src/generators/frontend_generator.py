import shutil
from pathlib import Path


def generate_frontend(preset: str, name: str):
    template_dir = Path(__file__).parent.parent / "templates" / "frontend" / preset

    # Create target directory if it doesn't exist
    target_dir = Path(f"{name}.frontend")
    target_dir.mkdir(parents=True, exist_ok=True)

    # Copy template files to target directory
    if template_dir.exists():
        shutil.copytree(template_dir, target_dir, dirs_exist_ok=True)
    else:
        raise FileNotFoundError(f"Frontend preset template '{preset}' not found")
