# -*- coding: utf-8 -*-
# @Time : 2021/10/9 16:10
# @Author : YangYu
# @Email: yangyu.cs@outlook.com
# @File : serializers.py
# @Software: PyCharm
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import *


class ChapterSerializer(ModelSerializer):
    class Meta:
        model = Chapter
        fields = '__all__'


class lessonBriefSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['LessonID', 'LessonName', 'cover_clip', 'detail']


class LessonSerializer(ModelSerializer):
    """
    课程序列化器
    """
    chapters = serializers.SerializerMethodField(read_only=True)
    cover = serializers.ImageField(write_only=True)
    cover_clip = serializers.ImageField(read_only=True)

    def get_chapters(self, instance):
        """
        获取课程的章节列表
        """
        chapters = instance.chapters.all()
        res = []
        for chap in chapters:
            res.append({'id': chap.id,
                        'name': chap.ChapterName
                        })
        return res

    class Meta:
        model = Lesson
        fields = '__all__'


class learnerLessonSerializer(ModelSerializer):
    class Meta:
        model = LearnerLesson
        fields = '__all__'


class lessonBriefSerializer(serializers.ModelSerializer):
    cover_clip = serializers.ImageField(read_only=True)
    detail = serializers.CharField(read_only=True)

    class Meta:
        model = Lesson
        fields = ['id', 'LessonName', 'cover_clip', 'detail']
