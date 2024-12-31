# Generated by Django 5.1.3 on 2024-12-18 05:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0030_remove_customtask_subject_code_customtask_subject_id'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='customclassschedule',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='customclassschedule',
            name='student_id',
        ),
        migrations.RemoveField(
            model_name='customclassschedule',
            name='subject',
        ),
        migrations.AlterUniqueTogether(
            name='customsubject',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='customsubject',
            name='semester_id',
        ),
        migrations.RemoveField(
            model_name='customsubject',
            name='student_id',
        ),
        migrations.RemoveField(
            model_name='customtask',
            name='subject_id',
        ),
        migrations.RemoveField(
            model_name='customtask',
            name='subject_code',
        ),
        migrations.RemoveField(
            model_name='customtask',
            name='student_id',
        ),
        migrations.DeleteModel(
            name='AttendedClass',
        ),
        migrations.DeleteModel(
            name='CustomClassSchedule',
        ),
        migrations.DeleteModel(
            name='CustomSubject',
        ),
        migrations.DeleteModel(
            name='CustomTask',
        ),
    ]