# Generated by Django 5.1.3 on 2024-11-24 08:32

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_alter_customsemester_semester_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customclass',
            name='student_id',
        ),
        migrations.RemoveField(
            model_name='customclass',
            name='subject_code',
        ),
        migrations.CreateModel(
            name='CustomClassSchedule',
            fields=[
                ('classsched_id', models.AutoField(primary_key=True, serialize=False)),
                ('day_of_week', models.CharField(max_length=2)),
                ('scheduled_start_time', models.TimeField()),
                ('scheduled_end_time', models.TimeField()),
                ('room', models.CharField(max_length=75)),
                ('student_id', models.ForeignKey(db_column='student_id', on_delete=django.db.models.deletion.CASCADE, related_name='scheduled_classes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='attendedclass',
            name='classched_id',
            field=models.ForeignKey(db_column='classsched_id', on_delete=django.db.models.deletion.CASCADE, related_name='attendedclass', to='api.customclassschedule'),
        ),
        migrations.CreateModel(
            name='CustomSubject',
            fields=[
                ('subject_code', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('subject_title', models.CharField(max_length=255)),
                ('semester_id', models.ForeignKey(db_column='semester_id', on_delete=django.db.models.deletion.CASCADE, related_name='subsems', to='api.customsemester')),
                ('student_id', models.ForeignKey(db_column='student_id', on_delete=django.db.models.deletion.CASCADE, related_name='subjects', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='customclassschedule',
            name='subject_code',
            field=models.ForeignKey(db_column='subject_code', on_delete=django.db.models.deletion.CASCADE, related_name='classes', to='api.customsubject'),
        ),
        migrations.DeleteModel(
            name='CustomSub',
        ),
        migrations.DeleteModel(
            name='CustomClass',
        ),
    ]
