# Generated by Django 3.1 on 2020-08-20 18:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20200820_2054'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='created',
        ),
    ]
