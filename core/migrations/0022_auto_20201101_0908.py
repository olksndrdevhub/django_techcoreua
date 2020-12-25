# Generated by Django 3.0.8 on 2020-11-01 09:08

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0021_auto_20201022_0917'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=autoslug.fields.AutoSlugField(allow_unicode=True, editable=True, max_length=200, populate_from='title', unique=True),
        ),
        migrations.AlterField(
            model_name='tags',
            name='slug',
            field=autoslug.fields.AutoSlugField(allow_unicode=True, editable=True, max_length=200, populate_from='title', unique=True),
        ),
    ]