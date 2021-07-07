from django.db import models


# Create your models here.

class User(models.Model):
    username = models.CharField("用户名", max_length=30, unique=True)
    password = models.CharField("密码", max_length=32)
    phoneNumber = models.CharField("电话号码", max_length=20)
    group = models.IntegerField("用户类型")
    create_time = models.DateTimeField("创建时间", auto_now_add=True)

    def __str__(self):
        return 'username %s' %(self.username)
