# Generated by Django 3.2.4 on 2021-07-01 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20210701_0128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='added_date',
            field=models.CharField(default='', max_length=10),
        ),
    ]
