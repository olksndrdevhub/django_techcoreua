# Generated by Django 3.0.8 on 2020-08-01 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_post_preview_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(default='Windows 10', max_length=100, verbose_name='Категорія'),
            preserve_default=False,
        ),
    ]
