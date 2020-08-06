from django.db import models
from django.urls import reverse

from autoslug import AutoSlugField


import re


class Category(models.Model):
    title = models.CharField(max_length=50, verbose_name='Категорія')
    slug = AutoSlugField(populate_from='title',
                        unique=True,
                        allow_unicode=True,
                        max_length=200)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('core:category_page', kwargs={'slug': self.slug})

    class Meta:
        verbose_name_plural = 'Категорії'



class Post(models.Model):
    title = models.CharField(max_length=150, verbose_name='Назва')
    main_image = models.ImageField(verbose_name='Головне фото', upload_to='uploads/main_images')
    preview_text = models.CharField(verbose_name='Текст-прев\`ю', max_length=150)
    text = models.CharField(max_length=10000, verbose_name='Текст')
    slug = AutoSlugField(populate_from='title',
                        unique=True,
                        allow_unicode=True,
                        max_length=200)
    creating_date = models.DateTimeField(verbose_name='Дата створення', auto_now_add=True)
    category = models.ManyToManyField(Category)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'slug': self.slug})
    
    class Meta:
        verbose_name_plural = 'Пости'
        ordering = ('id',)