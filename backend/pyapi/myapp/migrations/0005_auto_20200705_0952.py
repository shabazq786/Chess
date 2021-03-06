# Generated by Django 3.0.8 on 2020-07-05 09:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_auto_20200705_0948'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='id',
        ),
        migrations.AddField(
            model_name='post',
            name='post_id',
            field=models.CharField(blank=True, default='5B8A0A', max_length=50, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AddField(
            model_name='user',
            name='user_id',
            field=models.CharField(blank=True, default='923059', max_length=50, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment_id',
            field=models.CharField(blank=True, default='4CC512', max_length=50, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='posted_date',
            field=models.CharField(default=datetime.datetime(2020, 7, 5, 9, 52, 44, 239216), max_length=50),
        ),
        migrations.AlterField(
            model_name='post',
            name='last_posted_date',
            field=models.CharField(default=datetime.datetime(2020, 7, 5, 9, 52, 44, 238787), max_length=50),
        ),
        migrations.AlterField(
            model_name='post',
            name='posted_date',
            field=models.CharField(default=datetime.datetime(2020, 7, 5, 9, 52, 44, 238748), max_length=50),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=50),
        ),
    ]
