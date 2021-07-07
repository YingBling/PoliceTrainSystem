# -*- coding: utf-8 -*-
# @Time : 2021/7/6 16:23
# @Author : YangYu
# @Email: yangyu.cs@outlook.com
# @File : views.py
# @Software: PyCharm
from django.http import HttpResponse
from django.shortcuts import render


def login_view(request):
    # 登录页面，
    # uname = request.POST['uname']
    # password = request.POST['password']
    # return HttpResponse('登录成功！')
    return render(request, 'login.html')

