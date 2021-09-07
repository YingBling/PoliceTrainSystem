# Generated by Django 3.2.4 on 2021-09-07 16:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rbac', '0008_auto_20210903_1039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='dept',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='rbac.dept', verbose_name='所属部门'),
        ),
        migrations.AlterField(
            model_name='user',
            name='post',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='rbac.post', verbose_name='所属岗位'),
        ),
    ]