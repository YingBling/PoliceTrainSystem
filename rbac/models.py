from django.db import models

# Create your models here.
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class Menu(models.Model):
    """
    菜单实体
    title
    """
    title = models.CharField(verbose_name='菜单名称', max_length=32, unique=True)
    icon = models.CharField(verbose_name='菜单图标地址', max_length=32, null=True, blank=True)

    class Meta:
        verbose_name = "菜单"
        verbose_name_plural = verbose_name

    def __str__(self):
        return f"{self.title}"


class Permission(models.Model):
    '''
    权限表
    '''
    # type = models.Choices
    title = models.CharField(max_length=32, verbose_name="权限名称")
    url = models.CharField(max_length=128, verbose_name="接口URL", null=True, blank=True)
    path = models.CharField(max_length=128, verbose_name='前端路由path', null=True, blank=True)
    # 权限关联菜单
    menu = models.ForeignKey('rbac.Menu', verbose_name='菜单', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "权限"
        verbose_name_plural = verbose_name

    def __str__(self):
        return f"{self.title}"


class Role(models.Model):
    '''
    角色表
    '''
    title = models.CharField(verbose_name="角色名称", max_length=32)
    permissions = models.ManyToManyField('rbac.Permission', verbose_name="角色所有权限", blank=True)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "角色"
        verbose_name_plural = verbose_name


class Dept(models.Model):
    '''
    部门表
    '''
    title = models.CharField(verbose_name="部门名称", max_length=32)
    parentDept = models.ForeignKey('self', verbose_name="上级部门", null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "部门"
        verbose_name_plural = verbose_name


class Post(models.Model):
    '''
    岗位表
    '''
    title = models.CharField(verbose_name="岗位名称", max_length=32)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "岗位"
        verbose_name_plural = verbose_name


class UserManager(BaseUserManager):
    '''
    用户管理器
    '''

    def create_user(self, username, password=None):
        '''
        创建用户
        '''
        if not username:
            raise ValueError('用户名不能为空')
        user = self.model(username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None):
        '''
        创建超级用户,django-admin后台的方法
        '''
        user = self.create_user(username=username, password=password)
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    username = models.CharField(verbose_name="用户名", max_length=30, unique=True)
    name = models.CharField(verbose_name='用户姓名', max_length=128, blank=True, null=True)
    email = models.CharField(verbose_name='邮件地址', max_length=100, blank=True, null=True)
    avatar = models.ImageField(verbose_name='个人照片', blank=True, null=True)
    gender = models.CharField(verbose_name='性别', blank=True, null=True, max_length=20)
    is_active = models.BooleanField(verbose_name='用户状态', default=True)
    is_admin = models.BooleanField(verbose_name='是否为管理员', default=False)
    create_time = models.DateTimeField("创建时间", auto_now_add=True)
    dept = models.ForeignKey('rbac.Dept', verbose_name="所属部门", on_delete=models.SET_NULL, blank=True, null=True)
    roles = models.ManyToManyField('rbac.Role', verbose_name="关联角色", db_constraint=False)
    post = models.ForeignKey('rbac.Post', verbose_name="所属岗位", on_delete=models.SET_NULL, blank=True, null=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'  # 用户标识符

    # REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.username

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        # django-admin后台的命令
        return self.is_admin

    class Meta:
        # 元数据
        verbose_name = "用户"
        verbose_name_plural = verbose_name
