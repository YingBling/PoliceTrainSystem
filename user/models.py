from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class User(AbstractBaseUser):
    username = models.CharField("用户名", max_length=30, unique=True)
    password = models.CharField("密码", max_length=32)
    phoneNumber = models.CharField("电话号码", max_length=20, default='0')
    group = models.IntegerField("用户组", default=0)
    create_time = models.DateTimeField("创建时间", auto_now_add=True)
    USERNAME_FIELD = 'username'

    def __str__(self):
        return 'username %s' % (self.username)
