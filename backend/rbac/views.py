from django.db import transaction

# Create your views here
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status

from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from utils.response import APIResponse
from .serializers import *
from rest_framework.views import APIView
import xlrd


class CustomPageNumberPagination(PageNumberPagination):
    """
    自定义分页器
    """
    page_size = 5  # 默认为5
    page_query_param = 'page'
    page_size_query_param = 'size'
    max_page_size = 20


class MenuViewSet(ModelViewSet):
    authentication_classes = []
    permission_classes = []
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


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
            return APIResponse(data=user_ser.data)
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


class ImportUser(APIView):
    """
    批量导入用户，并存入数据库中
    """
    authentication_classes = []
    permission_classes = []

    def post(self, request):
        gender_dict = {'男': 1, '女': 0}
        status_dict = {'启用': 1, '禁用': 0}
        # 获取用户文件
        file = request.FILES.get('users_file')
        excel_type = file.name.split('.')[1]
        if excel_type not in ['xls', 'xlsx']:
            return APIResponse(code=100, msg='导入用户数据失败')
        # 解析工作表
        wb = xlrd.open_workbook(filename=None, file_contents=file.read())
        # wb = openpyxl.load_workbook(file)
        table = wb.sheets()[0]  # 可迭代列表
        nrows = table.nrows
        try:
            with transaction.atomic():
                sql_list = []
                for i in range(1, nrows):
                    row_value = table.row_values(i)
                    sql_list.append(User(username=row_value[0], password=make_password(row_value[1]), name=row_value[2],
                                         gender=gender_dict[row_value[3]], email=row_value[4],
                                         is_active=status_dict[row_value[5]]))
                User.objects.bulk_create(sql_list)
        except Exception as e:
            return APIResponse(code=100, msg=str(e))
        return APIResponse(code=200, msg='导入用户数据成功')


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # authentication_classes = []  # 认证类
    permission_classes = []  # 权限类
    pagination_class = CustomPageNumberPagination  # 分页器
    filter_fields = ['name', 'dept', 'role', 'post']  # 过滤器
    ordering_fields = ['id', 'dept']  # 排序

    @swagger_auto_schema(
        operation_summary='用户信息',
        operation_description='获取用户信息',
        responses={status.HTTP_200_OK: UserInfoSerializer}
    )
    def get_user_info(self, request):
        """
        获取用户的用户名，id，头像等等
        """
        user = request.user
        roles = user.role.all()
        serializer = UserInfoSerializer(user)
        return APIResponse(data=serializer.data)

    @action(methods=['GET'], detail=False)
    def get_menu_button(self, request, *args, **kwargs):
        """
        1.获取登录用户
        2.获取用户的所有角色
        3.获取角色的菜单，按钮
        4.返回树形菜单
        """
        user = request.user
        roles = user.role.all()
        if roles.count() == 0:
            raise Exception('当前用户未分配角色')
        menu_list = Menu.objects.none()
        button_list = MenuButton.objects.none()

        for role in roles:
            menu_list = menu_list | role.menus.all()
            button_list = button_list | role.permissions.all()
        menu_list = menu_list.distinct()
        button_list = button_list.distinct()
        menu_ser = MenuSerializer(menu_list, many=True)
        button_ser = MenuButtonSerializer(button_list, many=True)
        return APIResponse(data={
            'menu_list': menu_ser.data,
            'button_list': button_ser.data
        })

    @swagger_auto_schema(
        operation_summary='用户菜单',
        operation_description='获取该用户的所有菜单',
        responses={status.HTTP_200_OK: MenuTreeSerializer}
    )
    def get_menus(self, request):
        user = request.user
        # 用户所有的角色
        roles = user.role.all()
        for role in roles:
            menus = role.menus.all()
            root_menus = Menu.objects.none()
            for m in menus:
                if m.parent == None:
                    root_menus = root_menus | m
            # print(root_menus)
            serializer = MenuTreeSerializer(instance=root_menus, context={'menus': menus})
            return Response(serializer.data)


class DeptViewSet(ModelViewSet):
    queryset = Dept.objects.all()
    serializer_class = DeptSerializer
    authentication_classes = []
    # test
    permission_classes = []
    pagination_class = CustomPageNumberPagination

    def get_serializer_class(self):
        if self.action == 'get_dept_tree':
            return SubDeptSerializer
        else:
            return DeptSerializer

    @action(methods=['GET'], detail=True)
    def get_dept_tree(self, request, **kwargs):
        """
        获取部门树
        test
        """
        # root = self.get_queryset().filter(parent=None).first()
        instance = self.get_object()
        serializer = self.get_serializer(instance=instance)
        return APIResponse(data=serializer.data)


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    authentication_classes = []
    permission_classes = []


class RoleViewSet(ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
