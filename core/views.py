from django.shortcuts import render

from .models import Category, Post

def index(request):
    posts = Post.objects.all()
    categories = Category.objects.all()
    return render(request, 'home.html', context={'posts': posts, 'categories': categories})


def category_page(request, slug):
    categories = Category.objects.all()
    print(slug)
    category = Category.objects.filter(slug=slug).first()
    posts = Post.objects.filter(category=category)
    print(posts)
    return render(request, 'category-page.html', context={'posts': posts, 'categories': categories})