# Generated by Django 3.1 on 2020-09-30 15:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0007_auto_20200930_2032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todoitem',
            name='deadline',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
