# Generated by Django 3.1 on 2020-09-30 14:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0005_auto_20200920_0125'),
    ]

    operations = [
        migrations.AddField(
            model_name='todoitem',
            name='deadline',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]