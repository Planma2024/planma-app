# Generated by Django 5.1.3 on 2025-02-06 08:55

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0036_customuser_profile_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendedclass',
            name='attendance_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.RemoveField(
            model_name='attendedclass',
            name='date',
        ),
        migrations.AlterUniqueTogether(
            name='attendedclass',
            unique_together={('classsched_id', 'attendance_date')},
        ),
    ]
