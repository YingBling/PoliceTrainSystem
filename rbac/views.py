from django.shortcuts import render

# Create your views here
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from .models import *
from .serializers import *
from rest_framework.views import APIView


class CustomPageNumberPagination(PageNumberPagination):
    """
    自定义分页器
    """
    page_size = 5  # 默认为5
    page_query_param = 'page'
    page_size_query_param = 'size'
    max_page_size = 20


# 获取系统的全部权限
class ListPermission(APIView):
    def get(self, request):
        permissions = Permission.objects.all()
        perms_ser = PermissionSerializer(permissions, many=True)
        return Response(perms_ser.data)


class ListPost(APIView):
    def get(self, request):
        posts = Post.objects.all()
        posts_ser = PostSerializer(posts, many=True)
        return Response(posts_ser.data)


class UserAPIView(APIView):
    '''
    用户视图
    '''
    authentication_classes = []
    permission_classes = []

    def get(self, request, *args, **kwargs):
        # 如果关键字参数中有pk的话是查询单个用户
        if kwargs.get('pk', None):
            user = User.objects.filter(pk=kwargs.get('pk')).first()
            user_ser = UserSerializer(user)
        # 如果关键字参数中没有pk，则返回全部用户信息
        else:
            users = User.objects.all().filter(is_active=True)
            page_num = CustomPageNumberPagination()
            users_ser = UserSerializer(page_num.paginate_queryset(users, request, view=self)
                                       , many=True)
            return Response(data=users_ser.data)

    def post(self, request, *args, **kwargs):
        if isinstance(request.data, dict):
            # 如果request.data对象传来的是字典对象的话，说明新增一条数据
            user_ser = UserSerializer(data=request.data)
            user_ser.is_valid(raise_exception=True)
            user_ser.save()
            return Response(data=user_ser.data)
        elif isinstance(request.data, list):
            # 如果request.data对象传来的是数组对象的话，说明新增一组数据
            user_ser = UserSerializer(data=request.data, many=True)
            user_ser.is_valid(raise_exception=True)
            user_ser.save()
            return Response(data=user_ser.data)

    def put(self, request, *args, **kwargs):
        if kwargs.get('pk'):
            user = User.objects.filter(pk=kwargs.get('pk')).first()
            user_ser = UserSerializer(instance=user, data=request.data)
            user_ser.is_valid(raise_exception=True)
            user_ser.save()
            return Response(data=user_ser.data)
        else:
            # 改多个
            user_list = []  # 用户对象列表
            modify_data = []  # 更改的数据列表
            for item in request.data:
                pk = item.pop('id')
                user = User.objects.filter(pk=pk).first()
                user_list.append(user)
                modify_data.append(item)
            # user_ser = UserSerializer(instance=user_list, data=modify_data, many=True)
            # user_ser.is_valid()
            # user_ser.save()
            for index, data in enumerate(modify_data):
                user_ser = UserSerializer(instance=user_list[index], data=data)
                user_ser.is_valid()
                user_ser.save()
            user_ser = UserSerializer(user_list, many=True)
            return Response(user_ser.data)

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        pks = []
        if pk:
            # 单条删除
            pks.append(pk)
        else:
            # 多条删除
            pks = request.data['pks']
        ret = User.objects.filter(pk__in=pks, is_active=True).update(is_active=False)
        if ret:
            return Response("删除成功")
        else:
            return Response("没有要删除的数据")


class UserView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = []  # 认证类
    permission_classes = []  # 权限类
    pagination_class = CustomPageNumberPagination  # 分页器
    filter_fields = ['name', 'dept', 'roles', 'post']  # 过滤器
    ordering_fields = ['id', 'dept']  # 排序


class ListDept(APIView):
    def get(self, request):
        depts = Dept.objects.all()
        depts_ser = DeptSerializer(depts, many=True)
        return Response(depts_ser.data)


class ListRole(APIView):
    def get(self, request):
        roles = Role.objects.all()
        roles_ser = RoleSerializer(roles, many=True)
        return Response(roles_ser.data)
