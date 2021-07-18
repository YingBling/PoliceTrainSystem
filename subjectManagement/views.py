from django.shortcuts import render

# Create your views here.
from user.models import User
from .models import Lesson
from rest_framework import viewsets
from rest_framework import permissions
from .serializer import LessonSerializer


# 视图类-继承modelviewset
class LessonViewSet(viewsets.ModelViewSet):
    try:
        queryset = User.objects.all()  # 所有的课程
        serializer_class = LessonSerializer
    except Exception as e:
        print(e)
