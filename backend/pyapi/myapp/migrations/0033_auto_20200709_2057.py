# Generated by Django 3.0.8 on 2020-07-09 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0032_auto_20200709_2049'),
    ]

    operations = [
        migrations.AddField(
            model_name='rate',
            name='rate_id',
            field=models.CharField(default='', max_length=50, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='rate',
            name='username',
            field=models.CharField(max_length=50),
        ),
    ]
