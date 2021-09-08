# -*- coding: utf-8 -*-
# @Time : 2021/8/30 11:20
# @Author : YangYu
# @Email: yangyu.cs@outlook.com
# @File : urls.py
# @Software: PyCharm
from django.urls import path, re_path
from . import views, utils

# namespace
app_name = "rbac"
urlpatterns = [
    re_path(r'^login/$', utils.LoginView.as_view()),
    # re_path(r'^login/$', token_obtain_pair),
    re_path(r'^logout/$', utils.LogoutView.as_view()),
    re_path(r'^users/$', views.UserAPIView.as_view()),
    # 测试分支
    re_path(r'^users2/$', views.UserView.as_view()),  # 继承ListAPIView
    re_path(r'^users/(?P<pk>\d+)/$', views.UserAPIView.as_view()),
    re_path(r'^update-password/$', utils.UpdatePasswordView.as_view()),
    path('permission/list/', views.ListPermission.as_view()),
    path('dept/list/', views.ListDept.as_view()),
    path('role/list/', views.ListRole.as_view()),
    path('post/list/', views.ListPost.as_view()),
    ### test1
    ## test2
]
