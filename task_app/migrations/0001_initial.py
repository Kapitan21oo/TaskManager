# Generated by Django 4.1.7 on 2023-03-19 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('description', models.TextField(blank=True, null=True)),
                ('date_create', models.DateTimeField(auto_now_add=True)),
                ('condition', models.BooleanField(default=False)),
            ],
        ),
    ]