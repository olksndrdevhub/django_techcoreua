from django.db import models
from django.urls import reverse

from autoslug import AutoSlugField


import re


class Category(models.Model):
    title = models.CharField(max_length=50, verbose_name='Категорія')
    slug = AutoSlugField(populate_from='title',
                        unique=True,
                        allow_unicode=True,
                        max_length=200, editable=True)
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('core:category_page', kwargs={'slug': self.slug})

    class Meta:
        verbose_name_plural = 'Категорії'

class Tags(models.Model):
    title = models.CharField(max_length=50, verbose_name='Назва')
    slug = AutoSlugField(populate_from='title',
                        unique=True,
                        allow_unicode=True,
                        max_length=200)
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('core:tag_page', kwargs={'slug': self.slug})
    
    class Meta:
        verbose_name_plural = 'Теги'
        ordering = ('id',)


class Post(models.Model):
    title = models.CharField(max_length=150, verbose_name='Назва')
    main_image = models.ImageField(verbose_name='Головне фото', upload_to='uploads/main_images')
    preview_text = models.CharField(verbose_name='Текст-прев\`ю', max_length=300)
    text = models.CharField(max_length=20000, verbose_name='Текст')
    slug = AutoSlugField(populate_from='title',
                        unique=True,
                        allow_unicode=True,
                        max_length=200,
                        editable=True)
    
    creating_date = models.DateTimeField(verbose_name='Дата створення', auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tags, verbose_name='Теги')
    star = models.BooleanField(verbose_name='Star', default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('core:post_page', kwargs={'slug': self.slug})
    
    class Meta:
        verbose_name_plural = 'Пости'
        ordering = ('-creating_date',)

