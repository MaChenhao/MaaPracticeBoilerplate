from pathlib import Path

import shutil, os

assets_dir = Path(__file__).parent.resolve() / "assets"


def configure_ocr_model():
    assets_ocr_dir = assets_dir / "MaaCommonAssets" / "OCR"
    if not assets_ocr_dir.exists():
        print(f"File Not Found: {assets_ocr_dir}")
        exit(1)

    ocr_dir = assets_dir / "resource" / "model" / "ocr"
    if not ocr_dir.exists():  # copy default OCR model only if dir does not exist
        shutil.copytree(
            assets_dir / "MaaCommonAssets" / "OCR" / "ppocr_v5" / "zh_cn",
            ocr_dir,
            dirs_exist_ok=True,
        )
    else:
        print("Found existing OCR directory, skipping default OCR model import.")


def configure_dep():
    dep_dir = Path(__file__).parent.parent / "deps"
    dep_target = Path(__file__).parent / "deps"
    if not dep_target.exists():
        os.symlink(dep_dir, dep_target, target_is_directory=True)


if __name__ == "__main__":
    configure_dep()
    configure_ocr_model()

    print("OCR model configured.")
