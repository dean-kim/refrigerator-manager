# Generated by Django 2.0.4 on 2018-06-27 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0004_auto_20180627_0502'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forks',
            name='quantity',
            field=models.IntegerField(),
        ),
    ]