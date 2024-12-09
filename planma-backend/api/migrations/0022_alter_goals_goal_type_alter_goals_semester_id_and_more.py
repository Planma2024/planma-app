# Generated by Django 5.1.3 on 2024-12-09 09:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0021_remove_userpref_notification_enabled'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goals',
            name='goal_type',
            field=models.CharField(choices=[('Academic', 'Academic'), ('Personal', 'Personal')], max_length=30),
        ),
        migrations.AlterField(
            model_name='goals',
            name='semester_id',
            field=models.ForeignKey(blank=True, db_column='semester_id', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='goalsems', to='api.customsemester'),
        ),
        migrations.AlterField(
            model_name='goals',
            name='target_hours',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='goals',
            name='timeframe',
            field=models.CharField(choices=[('Daily', 'Daily'), ('Weekly', 'Weekly'), ('Monthly', 'Monthly')], max_length=20),
        ),
    ]
