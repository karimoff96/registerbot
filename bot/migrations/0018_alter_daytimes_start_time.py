# Generated by Django 4.2.1 on 2023-05-30 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0017_alter_daytimes_start_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='daytimes',
            name='start_time',
            field=models.TimeField(default='06:07', unique=True),
        ),
    ]
