# Generated by Django 3.0.8 on 2020-07-10 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0033_auto_20200709_2057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rate',
            name='rate_id',
            field=models.CharField(max_length=50, primary_key=True, serialize=False, unique=True),
        ),
    ]
