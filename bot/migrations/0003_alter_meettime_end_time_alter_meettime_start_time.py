# Generated by Django 4.2.1 on 2023-05-26 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0002_patient_step_alter_meettime_end_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meettime',
            name='end_time',
            field=models.TimeField(default='12:00:04'),
        ),
        migrations.AlterField(
            model_name='meettime',
            name='start_time',
            field=models.TimeField(default='12:00:04'),
        ),
    ]
