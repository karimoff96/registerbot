# Generated by Django 4.2.1 on 2023-05-30 08:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0021_alter_times_start_time_alter_times_week_day'),
    ]

    operations = [
        migrations.CreateModel(
            name='Time',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.TimeField(default='08:28', unique=True)),
                ('end_time', models.TimeField(blank=True, null=True)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='WeekDay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('week_day', models.CharField(choices=[('monday', 'Dushanba'), ('tuesdan', 'Seshanba'), ('Chorshanba', 'Chorshanba'), ('Pashanba', 'Pashanba'), ('Juma', 'Juma'), ('Shanba', 'Shanba'), ('Yakshanba', 'Yakshanba')], default=3, max_length=20, unique=True)),
                ('end_time', models.TimeField(blank=True, null=True)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.AlterField(
            model_name='appointment',
            name='doctor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='bot.doctor'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='appointment',
            name='time',
            field=models.ManyToManyField(to='bot.time'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='week_day',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='bot.weekday'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='doctor',
            name='availabe_days',
            field=models.ManyToManyField(to='bot.weekday'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='busy_time',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='bot.time'),
        ),
        migrations.DeleteModel(
            name='Times',
        ),
    ]
