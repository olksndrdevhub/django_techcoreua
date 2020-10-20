# Generated by Django 3.0.8 on 2020-10-20 13:08

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_auto_20201020_1307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=autoslug.fields.AutoSlugField(allow_unicode=True, editable=False, max_length=30, populate_from='title', unique=True),
        ),
    ]