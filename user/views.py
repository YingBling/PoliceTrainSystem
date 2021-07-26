# from django.contrib.auth.models import User
from django.views.decorators.http import require_http_methods
from rest_framework.decorators import permission_classes, action
import hashlib
from .models import User
from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework import permissions
from .serializers import UserSerializer
from rest_framework_simplejwt.tokens import RefreshToken


# Create your views here.
# @require_http_methods(["POST"])
# def register_view(request):
#     resp = {'code': 201,
#             'msg': 'success',
#             'data': ''
#             }
#     serializer = UserSerializer(data=request)
#     if serializer.is_valid():
#         # 通过数据校验
#         serializer.save()
#         resp['data'] = serializer.data
#     else:
#         resp['code'] = 403
#         resp['msg'] = '数据校验失败'
#         resp['data'] = serializer.errors
#     return Response(resp)


# 登录&注册视图集，对所有用户开放
class LoginAndRegister(viewsets.ViewSet):
    def register(self, request):
        resp = {'code': 201,
                'msg': 'success',
                'data': ''
                }
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            # 通过数据校验
            serializer.save()
            resp['data'] = serializer.data
        else:
            resp['code'] = 403
            resp['msg'] = '数据校验失败'
            resp['data'] = serializer.errors
        return Response(resp)

    def login(self, request):
        resp = {
            'code': 200,
            'msg': 'success',
            'data': ''
        }
        m = hashlib.md5()
        username = request.data['username']
        password = request.data['password']
        m.update(password.encode())
        pwdhash = m.hexdigest()
        if username == "" or password == "":
            resp['code'] = 403
            resp['msg'] = '用户名或密码为空'
        else:
            user = User.objects.filter(username=username, password=pwdhash).first()
            if user:
                serializer = UserSerializer(user)
                refresh = RefreshToken.for_user(user)
                resp['data'] = str(refresh.access_token)  # 这里返回一个token
            else:
                resp['msg'] = '用户名或密码错误'
                resp['code'] = 404
        return Response(resp)


class UserViewSet(viewsets.ViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    # 注册一个新用户用户
    # def register(self, request):
    #     resp = {'code': 201,
    #             'msg': 'success',
    #             'data': ''
    #             }
    #     serializer = UserSerializer(data=request.data)
    #     if serializer.is_valid():
    #         # 通过数据校验
    #         serializer.save()
    #         resp['data'] = serializer.data
    #     else:
    #         resp['code'] = 403
    #         resp['msg'] = '数据校验失败'
    #         resp['data'] = serializer.errors
    #     return Response(resp)

    # if username == '' or password == '':
    #     resp = {
    #         'code': 401.1,
    #         'msg': '用户名或密码为空',
    #         'data': ''
    #     }
    #     return Response(resp, status=status.HTTP_403_FORBIDDEN)
    # user = User.objects.filter(username=username)  # 返回user的集合
    # if user.exists():  # 如果存在该用户的话
    #     resp = {
    #         'code': 401.2,
    #         'msg': '该用户已存在',
    #         'data': ''
    #     }
    #     return Response(resp)
    # else:
    #     m = hashlib.md5()
    #     m.update(password.encode())
    #     pwd = m.hexdigest()  # 用MD5加密密码
    #     user = User.objects.create(username=username, password=pwd)
    #     user.save()
    #     serializer = UserSerializer(user)
    #     resp = {
    #         'code': 200,
    #         'msg': 'success',
    #         'data': serializer.data
    #     }
    #     return Response(resp, status=status.HTTP_201_CREATED)

    def list(self, request):  # 这个接口不对外使用
        resp = {
            'code': 200,
            'msg': 'success'
        }
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        resp['data'] = serializer.data
        return Response(resp)

    # 查询用户的个人信息，这里只有用户自己能看见
    def retrieve(self, request, pk):
        resp = {
            'code': 200,
            'msg': 'success'
        }
        try:
            user = User.objects.get(username=pk)
        except User.DoesNotExist:
            resp['code'] = 404
            resp['msg'] = '该用户不存在'
            return Response(resp)
        serializer = UserSerializer(user)
        resp['data'] = serializer.data
        return Response(resp)

    def update(self, request, pk):
        resp = {'code': 200,
                'msg': 'success'}
        user = User.objects.filter(id=pk).first()
        user_serializer = UserSerializer(user, request.data)
        if user_serializer.is_valid():  # 验证数据是否正确
            user_serializer.save()
            resp['data'] = user_serializer.data
        else:
            resp['code'] = 401
            resp['msg'] = '数据校验失败'
            resp['data'] = user_serializer.errors
        return Response(resp)
