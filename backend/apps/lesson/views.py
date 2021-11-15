# -*- coding: utf-8 -*-
# @Time : 2021/10/9 16:17
# @Author : YangYu
# @Email: yangyu.cs@outlook.com
# @File : views.py
# @Software: PyCharm
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .serializers import *
from .models import *


class chapterViewSet(ModelViewSet):
    authentication_classes = []
    permission_classes = []
    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializer


class lessonViewSet(ModelViewSet):
    authentication_classes = []
    permission_classes = []
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

    def get_chapterByLesson(self, request):
        """
        查询课程对应的章节信息
        """
        lesson_id = request.query_params['id']
        lesson = Lesson.objects.get(id=lesson_id)
        chapters = lesson.chapters.all()
        chapters_serializers = ChapterSerializer(chapters, many=True, context={"request": request})
        return Response(chapters_serializers.data)

    def get_briefByLesson(self, request):
        """
        查询课程的简介信息
        """

        lesson_id = request.query_params['id']
        lesson = Lesson.objects.get(id=lesson_id)
        brief_serializer = lessonBriefSerializer(lesson, context={"request": request})
        return Response(brief_serializer.data)

    def get_user_lessons(self, request):
        user = request.user
        # print(user)
        lessons = user.lessons.all()
        # print(lessons)
        serializer = lessonBriefSerializer(lessons, many=True)
        return Response(serializer.data)


class learnerLessonViewSet(ModelViewSet):
    authentication_classes = []
    permission_classes = []
    queryset = LearnerLesson.objects.all()
    serializer_class = learnerLessonSerializer
