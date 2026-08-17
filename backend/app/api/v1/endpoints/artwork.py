from fastapi import APIRouter, File, UploadFile

from app.services.artwork_service import ArtworkService

router = APIRouter(
    prefix="/artwork",
    tags=["Artwork"],
)


@router.post("/upload")
async def upload_artwork(
    file: UploadFile = File(...),
):
    """
    Upload and validate artwork image.
    """

    return await ArtworkService.upload(file)
