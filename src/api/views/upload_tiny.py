from rest_framework.response import Response
from rest_framework.views import APIView

from src.apps.storage.services import (
    create_public_media,
    get_public_file_url_by_id,
)


class UploadTiny(APIView):
    throttle_scope = "posts"

    def post(self, *args, **kwargs):
        file_obj = self.request.FILES["file"]
        file_name_suffix = file_obj.name.split(".")[-1]
        if file_name_suffix not in [
            "jpg",
            "png",
            "gif",
            "jpeg",
        ]:
            return Response({"message": "Wrong file format"})
        media_id = create_public_media(file_obj)
        file_url = get_public_file_url_by_id(media_id=media_id)
        return Response(
            {"message": "Image uploaded successfully", "location": file_url}
        )
