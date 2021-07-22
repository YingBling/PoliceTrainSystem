import json

from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from .models import Lesson
from django.core import serializers


# Create your views here.


@require_http_methods(["GET"])
def add_lessons(request):
    response = {}
    try:
        lesson = Lesson(name=request.GET["name"], details=request.GET["details"], pre_lesson=request.GET['prel'])
        lesson.save()  # 保存到数据库中
        response['msg'] = 'success'
        response['err'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['err'] = 1
    return JsonResponse(response)


@require_http_methods(["GET"])
def show_lessons(request):
    response = {}
    try:
        lessons = Lesson.objects.filter()
        response['data'] = json.loads(serializers.serialize("json", lessons))
        response['code'] = 200
        response['error'] = ''
    except Exception as e:
        response['data'] = {}
        response['code'] = 201
        response['error'] = str(e)
    return JsonResponse(response)
