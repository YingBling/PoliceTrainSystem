# Generated by Django 3.2.3 on 2021-07-07 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='group',
            field=models.IntegerField(verbose_name='用户类型'),
        ),
    ]
