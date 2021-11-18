# -*- coding: utf-8 -*-
# @Time : 2021/10/9 16:00
# @Author : YangYu
# @Email: yangyu.cs@outlook.com
# @File : urls.py
# @Software: PyCharm
from django.urls import re_path
from rest_framework.routers import SimpleRouter
from .views import *

router = SimpleRouter()
router.register('chapter', chapterViewSet)
router.register('lesson', lessonViewSet)
router.register('learner_lesson', learnerLessonViewSet)
urlpatterns = [
    re_path('lesson/get_user_lessons/', lessonViewSet.as_view({'get': 'get_user_lessons'})),
    re_path('lesson/get_chapterByLesson/',lessonViewSet.as_view({'get':'get_chapterByLesson'})),
    re_path('lesson/get_brief/',lessonViewSet.as_view({'get':'get_briefByLesson'}))
]
urlpatterns += router.urls
