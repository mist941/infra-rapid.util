import shutil
import sys
from pathlib import Path


def generate_frontend(preset: str, name: str):
    template_dir = Path(__file__).parent.parent / "templates" / "frontend" / preset

    # Create target directory if it doesn't exist
    target_dir = Path(f"{name}.frontend")
    target_dir.mkdir(parents=True, exist_ok=True)

    # Copy template files to target directory
    if template_dir.exists():
        shutil.copytree(template_dir, target_dir, dirs_exist_ok=True)

        # Run setup script if it exists
        setup_script = target_dir / "setup" / "setup.py"
        if setup_script.exists():
            import subprocess

            setup_script_abs = str(setup_script.absolute())
            subprocess.run(
                [sys.executable, setup_script_abs], cwd=target_dir, check=True
            )

            # Remove setup folder after running the script
            setup_folder = target_dir / "setup"
            shutil.rmtree(setup_folder)

    else:
        raise FileNotFoundError(f"Frontend preset template '{preset}' not found")
