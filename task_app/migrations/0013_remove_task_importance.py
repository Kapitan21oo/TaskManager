# Generated by Django 4.1.7 on 2023-03-27 09:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task_app', '0012_task_importance'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='importance',
        ),
    ]
