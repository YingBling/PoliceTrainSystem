# -*- coding: utf-8 -*-
# @Time : 2021/8/30 18:47
# @Author : YangYu
# @Email: yangyu.cs@outlook.com
# @File : utils.py.py
# @Software: PyCharm

from django.contrib.auth.hashers import make_password
from django.utils import timezone
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import token_obtain_pair, TokenObtainPairView, TokenRefreshView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework.views import APIView

from utils.response import APIResponse
from .models import User
from .serializers import UserSerializer


class LoginSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        username = attrs['username']
        password = attrs['password']
        user = User.objects.filter(username=username).first()
        if user and user.check_password(password):
            data = super().validate(attrs)
            refresh = self.get_token(user)
            data['id'] = self.user.id
            data['username'] = self.user.username
            data['last_login'] = self.user.last_login
            resp = {
                'code': 200,
                'data': data,
                'msg': '登录成功'

            }
        else:
            resp = {
                'code': 400,
                'data': None,
                'msg': '登录失败，用户名或密码错误！'
            }
        return resp


# 登录视图
class LoginView(TokenObtainPairView):
    authentication_classes = []
    permission_classes = []
    serializer_class = LoginSerializer


class LogoutView(APIView):
    """
    用户注销接口

    """
    def get(self, request):
        resp = {
            'code': 200,
            'msg': '用户退出系统'
        }
        user = request.user
        # 修改上次登录时间为注销时间
        user.last_login = timezone.now()
        user.save()  # 这里记得保存一下
        return APIResponse(resp)


# 更新密码视图
class ResetPasswordView(APIView):
    """
    更新密码视图
    """
    permission_classes = []

    def post(self, request):
        print(111111)
        resp = {
            'code': 200
        }
        username = request.data['username']
        old_password = request.data['old_password']
        new_password = request.data['new_password']
        user = User.objects.filter(username=username).first()
        if user and user.check_password(old_password):
            user.set_password(new_password)
            user.save()  # 这里记得保存一下，不然不会生效
            resp['msg'] = '修改成功'
        else:
            resp['code'] = 400
            resp['msg'] = '修改失败'
        return Response(resp)


class CustomResponse():
    def __init__(self):
        self.status = 100
        self.msg = 'success'

    @property
    def get_dict(self):
        return self.__dict__
