# Generated by Django 5.1.3 on 2025-03-20 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0038_scheduleentry'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customactivity',
            name='activity_desc',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='customevents',
            name='event_desc',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='customtask',
            name='task_desc',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='goals',
            name='goal_desc',
            field=models.TextField(blank=True, null=True),
        ),
    ]
