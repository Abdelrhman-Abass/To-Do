# Generated by Django 4.1.5 on 2023-02-21 11:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Tasks', '0007_task_uuid_userprofile_uuid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='uuid',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='uuid',
        ),
    ]