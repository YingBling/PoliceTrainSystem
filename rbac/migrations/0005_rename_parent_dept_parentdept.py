# Generated by Django 3.2.4 on 2021-08-30 06:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rbac', '0004_alter_post_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dept',
            old_name='parent',
            new_name='parentDept',
        ),
    ]