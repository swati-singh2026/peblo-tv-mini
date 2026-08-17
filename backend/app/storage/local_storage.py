from pathlib import Path
from uuid import uuid4

from fastapi import UploadFile


UPLOAD_DIR = Path("uploads/artwork")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)


def save_file(file: UploadFile, content: bytes) -> str:
    """
    Save uploaded file locally and return relative file path.
    """

    extension = Path(file.filename).suffix.lower()

    filename = f"{uuid4().hex}{extension}"

    file_path = UPLOAD_DIR / filename

    with open(file_path, "wb") as f:
        f.write(content)

    return str(file_path).replace("\\", "/")
