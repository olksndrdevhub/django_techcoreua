from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
from core.models import Post, Tags, Category

class PostSitemap(Sitemap):

    def items(self):
        return Post.objects.all()

class CategorySitemap(Sitemap):

    def items(self):
        return Category.objects.all()

class TagsSitemap(Sitemap):

    def items(self):
        return Tags.objects.all()