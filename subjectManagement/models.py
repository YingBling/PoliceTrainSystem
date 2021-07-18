from django.db import models
from rest_framework import serializers
# Create your models here.


# 课程类,一个课程包括多个科目，每个科目有前置科目，只有前置科目学习完了才可以学习下一个科目
class Subject(models.Model):
    name = models.CharField("课程名称", max_length=20, unique=True)
    period = models.IntegerField("学时", default=1)           # 学时
    details = models.CharField("课程详情", max_length=100)
    is_active = models.BooleanField("Status", default=True)   # 伪删除字段

    class Meta:
        db_table = 'subjectManagement_subject'
        verbose_name = '训练课程'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '%s_%d_%s' % (self.name, self.period, self.details)


# 科目
class Lesson(models.Model):
    name = models.CharField("科目名称", max_length=20, unique=True)
    details = models.CharField("科目详情", max_length=100)
    is_active = models.BooleanField("Status", default=True)
    pre_lesson = models.CharField("前置科目", max_length=20, default='')     # 这里先用文本表示吧，后面再想怎么设计
    subject = models.ManyToManyField(Subject)
