from fastapi import UploadFile

from app.storage.local_storage import save_file
from app.utils.image_validator import validate_image


class ArtworkService:
    @staticmethod
    async def upload(file: UploadFile) -> dict:
        """
        Validate and save uploaded artwork.
        """

        content = await validate_image(file)

        file_path = save_file(file, content)

        return {
            "message": "Artwork uploaded successfully.",
            "path": file_path,
        }
    