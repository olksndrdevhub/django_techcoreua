# Generated by Django 3.0.8 on 2020-09-13 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20200913_1448'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='star',
            field=models.BooleanField(default=False, verbose_name='Star'),
        ),
    ]