import os

from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView

from utils.response import APIResponse


class UploadFile(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request):
        file = request.FILES.get('file', None)
        if not file:
            return APIResponse(code=100, msg='上传文件为空')
        else:
            root_path = os.path.abspath('.')
            store_path = open(os.path.join("static", file.name), "wb+")
        for chunk in file.chunks():
            store_path.write(chunk)
        store_path.close()
        return APIResponse(code=200, msg='上传文件成功')
