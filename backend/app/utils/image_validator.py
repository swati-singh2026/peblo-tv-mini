from io import BytesIO

from fastapi import HTTPException, UploadFile, status
from PIL import Image

ALLOWED_TYPES = {
    "image/jpeg",
    "image/jpg",
    "image/png",
    "image/webp",
}

MAX_FILE_SIZE = 5 * 1024 * 1024  # 5 MB

MIN_WIDTH = 300
MIN_HEIGHT = 300

MAX_WIDTH = 4000
MAX_HEIGHT = 4000

ALLOWED_RATIOS = [
    round(16 / 9, 2),
    round(1 / 1, 2),
]


async def validate_image(file: UploadFile) -> bytes:
    """
    Validate uploaded image and return its bytes.
    """

    if file.content_type not in ALLOWED_TYPES:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Only JPG, JPEG, PNG and WEBP images are allowed.",
        )

    content = await file.read()

    if len(content) > MAX_FILE_SIZE:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Image size exceeds 5 MB.",
        )

    try:
        image = Image.open(BytesIO(content))
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid image file.",
        )

    width, height = image.size

    if width < MIN_WIDTH or height < MIN_HEIGHT:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Minimum dimensions are {MIN_WIDTH}x{MIN_HEIGHT}.",
        )

    if width > MAX_WIDTH or height > MAX_HEIGHT:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Maximum dimensions are {MAX_WIDTH}x{MAX_HEIGHT}.",
        )

    ratio = round(width / height, 2)

    if ratio not in ALLOWED_RATIOS:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Only 16:9 and 1:1 aspect ratios are allowed.",
        )

    await file.seek(0)

    return content