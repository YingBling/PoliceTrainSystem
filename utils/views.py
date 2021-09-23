from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet

from utils.response import APIResponse


class CustomModelViewSet(ModelViewSet):
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.isvalid(raise_exception=True)
        self.perform_create(serializer)
        return APIResponse(data=serializer.data)
