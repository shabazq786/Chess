# Generated by Django 3.0.8 on 2020-07-18 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0038_game_player'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='date',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
