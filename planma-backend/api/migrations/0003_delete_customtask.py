# Generated by Django 5.1.3 on 2024-11-15 16:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_rename_student_customtask_student_id'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CustomTask',
        ),
    ]
