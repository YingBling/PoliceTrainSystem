# Generated by Django 3.2.4 on 2021-09-02 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rbac', '0006_auto_20210902_1019'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='menu',
            options={'verbose_name': '菜单', 'verbose_name_plural': '菜单'},
        ),
        migrations.AlterField(
            model_name='menu',
            name='url',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
    ]
