# -*- coding: utf-8 -*-
# @Time : 2021/8/30 18:47
# @Author : YangYu
# @Email: yangyu.cs@outlook.com
# @File : utils.py.py
# @Software: PyCharm
from collections import OrderedDict

from django.utils import timezone
from django.utils.decorators import method_decorator
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenObtainSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from rest_framework.views import APIView

from utils.response import APIResponse
from .models import User


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
# @swagger_auto_schema(
#     responses={
#         '200': openapi.Response('获取成功')
#     },
#     security=[],
#     operation_id='captcha-get',
#     operation_description='获取用户信息',
# )
@method_decorator(name='post',
                  decorator=swagger_auto_schema(
                      operation_summary='用户登录',
                      operation_description='用户登录接口',
                      responses={status.HTTP_200_OK: openapi.Schema(
                          type=openapi.TYPE_OBJECT,
                          properties={"code": openapi.Schema(type=openapi.TYPE_NUMBER),
                                      "data": openapi.Schema(type=openapi.TYPE_OBJECT),
                                      "msg": openapi.Schema(type=openapi.TYPE_STRING)
                                      },
                          default={
                              "code": 200,
                              "data": {
                                  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYzNzMwNzE5MSwianRpIjoiOThhYjExYjFlNTcxNDFmN2JkOGExZjk4ODE1NTJjNTAiLCJ1c2VybmFtZSI6Inlhbmd5dSJ9.ZKor-UrfWxxPx2nEIA3GNV6Xtad3giLJTpMFPq9Rusc",
                                  "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjM3MzA3MTkxLCJqdGkiOiI3YmU5MTRkODBkNTc0YzMyOTU3MDlkYzdjN2E5OGI4NiIsInVzZXJuYW1lIjoieWFuZ3l1In0.8tndl_3p_ytdX_zssJI2v1DcAdbSCk1CEgZPHha0I0w",
                                  "id": 1,
                                  "username": "yangyu",
                                  "last_login": "2021-10-23T14:51:06.222534"
                              },
                              "msg": "登录成功"
                          }
                      ),
                          status.HTTP_400_BAD_REQUEST: openapi.Schema(
                              type=openapi.TYPE_OBJECT,
                              properties={
                                  "code": openapi.Schema(type=openapi.TYPE_NUMBER),
                                  "data": openapi.Schema(type=openapi.TYPE_STRING),
                                  "msg": openapi.Schema(type=openapi.TYPE_STRING),
                              },
                              default={
                                  "code": 400,
                                  "data": 'null',
                                  "msg": "登录失败，用户名或密码错误！"
                              }
                          )
                      }
                  ))
class LoginView(TokenObtainPairView):
    authentication_classes = []
    permission_classes = []
    serializer_class = LoginSerializer


class LogoutView(APIView):
    """
    用户注销接口
    """

    @swagger_auto_schema(operation_summary='注销登录',
                         operation_description='用户点击注销后，数据库中更新用户的last_login',
                         responses={status.HTTP_200_OK: openapi.Schema(
                             type=openapi.TYPE_OBJECT,
                             properties={
                                 "code": openapi.TYPE_NUMBER,
                                 "msg": openapi.TYPE_STRING
                             },
                             default={
                                 "code": 200,
                                 "msg": "用户退出系统"
                             }

                         )})
    def get(self, request):
        resp = {
            'code': 200,
            'msg': '用户退出系统'
        }
        user = request.user
        # 修改上次登录时间为注销时间
        user.last_login = timezone.now()
        user.save()  # 这里记得保存一下
        return Response(resp)


# 更新密码视图
class ResetPasswordView(APIView):
    """
    更新密码视图
    """
    permission_classes = []

    def post(self, request):
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
