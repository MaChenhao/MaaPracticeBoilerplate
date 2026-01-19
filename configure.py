from pathlib import Path

import shutil, os

assets_dir = Path(__file__).parent.resolve() / "assets"


def configure_dep():
    dep_dir = Path(__file__).parent.parent / "deps"
    dep_target = Path(__file__).parent / "deps"
    if not dep_target.exists():
        os.symlink(dep_dir, dep_target, target_is_directory=True)
    print("dep symlink configured.")


if __name__ == "__main__":
    configure_dep()
