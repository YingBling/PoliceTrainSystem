from django.db import models


# Create your models here.


class Chapter(models.Model):
    """
    章节实体，要求用户需要按照一定的学习顺序学习
    ChapterID：章节编号，唯一
    ChapterName：章节名称
    ChapterURL：章节的存放地址
    lessons：章节所属的课程，多对多关系，lesson.chapters可以查询课程下的所有章节
    learners：选修章节的学员，多对多关系，learner.chapters可以查询该学员选修的所有章节
    """
    ChapterID = models.CharField(unique=True, max_length=255, verbose_name='章节编号')
    ChapterName = models.CharField(max_length=255, verbose_name='章节名称', null=True, blank=True)
    ChapterURL = models.CharField(verbose_name='章节存放地址', max_length=255, null=True, blank=True)
    lessons = models.ManyToManyField('lesson.Lesson', related_name='chapters',
                                     through='lesson.ChapterLesson',
                                     through_fields=('chapter', 'lesson'),
                                     verbose_name='章节所属课程')
    learners = models.ManyToManyField('rbac.User', related_name='chapters',
                                      through='lesson.LearnerChapter',
                                      through_fields=('chapter', 'learner'))

    class Meta:
        verbose_name = '章节'
        verbose_name_plural = verbose_name

    def __str__(self):
        return f"{self.ChapterName}"


class LearnerChapter(models.Model):
    """
    学员章节表
    learner：学员实体，外键
    chapter：章节实体，外键
    status：学习状态，是否完成本章的学习
    """
    learner = models.ForeignKey('rbac.User', on_delete=models.CASCADE)
    chapter = models.ForeignKey('lesson.Chapter', on_delete=models.CASCADE)
    status = models.BooleanField(default=False, verbose_name='学习状态', null=True, blank=True)

    # score = models.DecimalField(default=0.0, verbose_name='章节成绩', blank=True)
    class Meta:
        verbose_name = "学员-章节"
        verbose_name_plural = verbose_name


class ChapterLesson(models.Model):
    """
    章节课程表
    lesson：课程实体，外键
    chapter：章节实体，外键
    prev：课程每一章节的前置章节，可为空，外键
    """
    lesson = models.ForeignKey('lesson.Lesson', on_delete=models.CASCADE)
    chapter = models.ForeignKey('lesson.Chapter', on_delete=models.CASCADE)
    prev = models.ForeignKey('lesson.Chapter',
                             blank=True,
                             null=True,
                             on_delete=models.CASCADE,
                             related_name='prev')

    class Meta:
        verbose_name = "课程-章节"
        verbose_name_plural = verbose_name


class Lesson(models.Model):
    """
    课程实体
    LessonID：课程编号，唯一
    LessonName：课程名称
    detail：课程的描述信息，可为空
    learners：学员，多对多关系,learner.lessons可以查询学员选修的所有课程
    """
    LessonID = models.CharField(unique=True, max_length=255, verbose_name='课程编号')
    LessonName = models.CharField(max_length=255, verbose_name='课程名称')
    detail = models.CharField(verbose_name='描述信息', max_length=255, blank=True, null=True)
    learners = models.ManyToManyField('rbac.User', related_name='lessons',
                                      through='lesson.LearnerLesson',
                                      through_fields=('lesson', 'learner'))

    class Meta:
        verbose_name = '课程'
        verbose_name_plural = verbose_name

    def __str__(self):
        return f"{self.LessonName}"


class LearnerLesson(models.Model):
    """
    学员课程表
    learner：学员实体，外键
    lesson：课程实体，外键
    status：学习状态，是否完成课程的学习，完成全部的章节时为True
    """
    learner = models.ForeignKey('rbac.User', on_delete=models.CASCADE)
    lesson = models.ForeignKey('lesson.Lesson', on_delete=models.CASCADE)
    status = models.BooleanField(verbose_name="学习状态", default=False, null=True, blank=True)

    class Meta:
        verbose_name = "学员-课程"
        verbose_name_plural = verbose_name
