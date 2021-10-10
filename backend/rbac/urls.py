# -*- coding: utf-8 -*-
# @Time : 2021/8/30 11:20
# @Author : YangYu
# @Email: yangyu.cs@outlook.com
# @File : urls.py
# @Software: PyCharm
from django.urls import re_path
from rest_framework import routers

from . import views

# 自动注册路由
router = routers.SimpleRouter()
router.register('user', views.UserViewSet)
router.register('post', views.PostViewSet)
router.register('role', views.RoleViewSet)
router.register('dept', views.DeptViewSet)
router.register('menu', views.MenuViewSet)
# router.register('permission', views.PermissionViewSet)
# namespace
# print(router.urls)
app_name = "rbac"
urlpatterns = [
    # re_path(r'^get_user_info/$', utils.LoginView.as_view()),
    re_path(r'^users/$', views.UserAPIView.as_view()),
    re_path(r'^users/(?P<pk>\d+)/$', views.UserAPIView.as_view()),
    re_path('import_user/', views.ImportUser.as_view())
]
urlpatterns += router.urls
