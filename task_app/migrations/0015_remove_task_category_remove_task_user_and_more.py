# Generated by Django 4.1.7 on 2023-03-28 18:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task_app', '0014_categorys_task_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='category',
        ),
        migrations.RemoveField(
            model_name='task',
            name='user',
        ),
        migrations.DeleteModel(
            name='Categorys',
        ),
    ]