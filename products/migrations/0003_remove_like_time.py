# Generated by Django 3.0.6 on 2020-06-10 07:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_like_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='like',
            name='time',
        ),
    ]
