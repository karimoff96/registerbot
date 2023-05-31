# Generated by Django 4.2.1 on 2023-05-30 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0029_patient_urgent_alter_time_start_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='time',
            name='start_time',
            field=models.TimeField(default='10:11', unique=True),
        ),
        migrations.AlterField(
            model_name='weekday',
            name='week_day',
            field=models.CharField(choices=[('Dushanba', 'Dushanba'), ('Seshanba', 'Seshanba'), ('Chorshanba', 'Chorshanba'), ('Pashanba', 'Pashanba'), ('Juma', 'Juma'), ('Shanba', 'Shanba'), ('Yakshanba', 'Yakshanba')], default=3, max_length=20, unique=True),
        ),
    ]
