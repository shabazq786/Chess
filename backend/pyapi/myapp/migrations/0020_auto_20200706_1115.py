# Generated by Django 3.0.8 on 2020-07-06 11:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0019_auto_20200705_1512'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='dislikes',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='likes',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='title',
        ),
    ]
