# Generated by Django 3.2.3 on 2021-06-30 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True, verbose_name='课程名称')),
                ('period', models.IntegerField(default=1, verbose_name='学时')),
                ('details', models.CharField(max_length=100, verbose_name='课程详情')),
                ('is_active', models.BooleanField(default=True, verbose_name='Status')),
            ],
            options={
                'verbose_name': '训练课程',
                'verbose_name_plural': '训练课程',
                'db_table': 'subject',
            },
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True, verbose_name='科目名称')),
                ('details', models.CharField(max_length=100, verbose_name='科目详情')),
                ('is_active', models.BooleanField(default=True, verbose_name='Status')),
                ('pre_lesson', models.CharField(default='', max_length=20, verbose_name='前置课程')),
                ('subject', models.ManyToManyField(to='subjectManagement.Subject')),
            ],
        ),
    ]