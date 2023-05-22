# Generated by Django 4.1.7 on 2023-03-27 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_app', '0011_task_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='importance',
            field=models.CharField(choices=[('important', 'Важная задача'), ('medium', 'Задача средней важности'), ('unimportant', 'Не важная задача')], default=None, max_length=20),
        ),
    ]
