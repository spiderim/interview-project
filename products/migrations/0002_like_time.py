# Generated by Django 3.0.6 on 2020-06-10 07:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='like',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 10, 12, 45, 4, 716180)),
            preserve_default=False,
        ),
    ]
