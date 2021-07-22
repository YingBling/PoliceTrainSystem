from django.db import models


# Create your models here.
class Lesson(models.Model):
    name = models.CharField("科目名称", max_length=20, unique=True)
    details = models.CharField("科目详情", max_length=100)
    is_active = models.BooleanField("Status", default=True)
    pre_lesson = models.CharField("前置科目", max_length=20, default='')  # 这里先用文本表示吧，后面再想怎么设计

    def __str__(self):
        return self.name + ',' + self.details + ',' + self.pre_lesson
