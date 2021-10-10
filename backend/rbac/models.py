from django.db import models

# Create your models here.
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class Button(models.Model):
    """
    按钮实体
    """
    name = models.CharField(verbose_name="按钮名称", max_length=32)
    value = models.CharField(verbose_name='权限值', max_length=32)


class Menu(models.Model):
    """
    """
    parent = models.ForeignKey(to='rbac.Menu', verbose_name='父级菜单',
                               db_constraint=False, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(verbose_name='菜单名称', max_length=128, unique=True)
    icon = models.CharField(verbose_name='菜单图标地址', max_length=128, null=True, blank=True)
    sort = models.IntegerField(default=1, verbose_name="显示排序",
                               null=True, blank=True, help_text="显示排序")
    path = models.CharField(verbose_name='路由地址', null=True, blank=True, max_length=128)

    class Meta:
        verbose_name = "菜单"
        verbose_name_plural = verbose_name

    def __str__(self):
        return f"{self.title}"


class MenuButton(models.Model):
    """
    菜单按钮
    """
    menu = models.ForeignKey(to="rbac.Menu", db_constraint=False, on_delete=models.SET_NULL, null=True)
    title = models.CharField(verbose_name="按钮名", max_length=128)
    value = models.CharField(verbose_name="权限值", max_length=128)
    url = models.CharField(verbose_name='接口地址', max_length=128)
    METHOD_CHOICES = (
        (0, "GET"),
        (1, "POST"),
        (2, "PUT"),
        (3, "DELETE")
    )
    method = models.IntegerField(choices=METHOD_CHOICES, default=0, null=True, blank=True, verbose_name="请求方法")

    class Meta:
        db_table = "rbac_menu_button"


class Role(models.Model):
    '''
    角色表
    '''
    title = models.CharField(verbose_name="角色名称", max_length=32)
    menus = models.ManyToManyField('rbac.Menu', verbose_name="角色所有菜单", db_constraint=False)
    permissions = models.ManyToManyField('rbac.MenuButton', verbose_name="角色所有权限", db_constraint=False)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "角色"
        verbose_name_plural = verbose_name


class Dept(models.Model):
    '''
    部门表
    '''
    title = models.CharField(verbose_name="部门名称", max_length=32, unique=True)
    parent = models.ForeignKey('self', verbose_name="上级部门", related_name='children_dept', null=True,
                               on_delete=models.SET_NULL)

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
    GENDER_CHOICES = (
        (0, "女"),
        (1, "男"),
    )
    gender = models.IntegerField(choices=GENDER_CHOICES, default=1, verbose_name='性别', blank=True, null=True)
    is_active = models.BooleanField(verbose_name='用户状态', default=True)
    is_admin = models.BooleanField(verbose_name='是否为管理员', default=False)
    create_time = models.DateTimeField("创建时间", auto_now_add=True)
    dept = models.ForeignKey('rbac.Dept', verbose_name="所属部门", on_delete=models.SET_NULL, blank=True, null=True)
    role = models.ManyToManyField('rbac.Role', verbose_name="关联角色", db_constraint=False)
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
        ordering = ['name']
