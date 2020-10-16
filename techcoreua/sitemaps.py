from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
from core.models import Post, Tags, Category

class PostSitemap(Sitemap):
    priority = 0.5
    changefreq = 'weekly'

    def items(self):
        return Post.objects.all()

class CategorySitemap(Sitemap):
    priority = 0.5
    changefreq = 'monthly'
    
    def items(self):
        return Category.objects.all()

class TagsSitemap(Sitemap):
    priority = 0.5
    changefreq = 'weekly'

    def items(self):
        return Tags.objects.all()

class StaticSitemap(Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return ['index', 'contacts', 'about', 'privacy']

    def location(self, item):
        return reverse(f'core:{item}')