# Generated by Django 3.1 on 2020-08-22 17:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_follow'),
    ]

    operations = [
        migrations.RenameField(
            model_name='follow',
            old_name='author',
            new_name='following',
        ),
    ]
