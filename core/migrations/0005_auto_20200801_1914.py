# Generated by Django 3.0.8 on 2020-08-01 19:14

import autoslug.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_post_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Категорія')),
                ('slug', autoslug.fields.AutoSlugField(allow_unicode=True, editable=False, max_length=200, populate_from='title', unique=True)),
            ],
            options={
                'verbose_name_plural': 'Категорії',
            },
        ),
        migrations.RemoveField(
            model_name='post',
            name='category',
        ),
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.ManyToManyField(to='core.Category'),
        ),
    ]
