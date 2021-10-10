from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Lesson)
admin.site.register(Chapter)
admin.site.register(LearnerChapter)
admin.site.register(LearnerLesson)
admin.site.register(ChapterLesson)