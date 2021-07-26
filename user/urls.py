# -*- coding: utf-8 -*-
# @Time : 2021/7/7 11:02
# @Author : YangYu
# @Email: yangyu.cs@outlook.com
# @File : urls.py
# @Software: PyCharm

from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('', views.UserViewSet)
urlpatterns = [
    path('all/', views.UserViewSet.as_view({'get': 'list'})),
    path('register/', views.LoginAndRegister.as_view({'post': 'register'})),
    path('login/', views.LoginAndRegister.as_view({'post': 'login'})),
    path('update/<int:pk>/', views.UserViewSet.as_view({'post': 'update'}))
]
