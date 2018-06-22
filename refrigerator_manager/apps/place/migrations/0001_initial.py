# Generated by Django 2.0.4 on 2018-06-22 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('FRIDGE', '냉동실'), ('FREEZER', '냉장실')], max_length=20)),
            ],
        ),
    ]
