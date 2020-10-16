from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic.list import ListView
from django.db.models import Q


from .models import Category, Post, Tags



def index(request):
    posts_list = Post.objects.all()

    page = request.GET.get('page', 1)
    paginator = Paginator(posts_list, 10)

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    tags = Tags.objects.all()
    categories = Category.objects.all()
    starres_posts = Post.objects.filter(star=True).all()
    s_p_1 = starres_posts[0]
    s_p_2 = starres_posts[1]
    s_p_3 = starres_posts[2]

    windows_posts = Post.objects.filter(category__title='Windows').all()
    linux_posts = Post.objects.filter(category__title='Linux').all()
    manuals_posts = Post.objects.filter(category__title='Мануали').all()

    last_windows_posts = windows_posts[0:3]
    last_linux_posts = linux_posts[0:3]
    last_manuals_posts = manuals_posts[0:3]

    context = {
        'posts': posts,
        's_p_1': s_p_1,
        's_p_2': s_p_2,
        's_p_3': s_p_3,
        'tags': tags,
        'posts': posts,
        'categories': categories,
        'last_windows_posts': last_windows_posts,
        'last_linux_posts': last_linux_posts,
        'last_manuals_posts': last_manuals_posts
    }
    return render(request, 'home.html', context=context)


def category_page(request, slug):
    tags = Tags.objects.all()
    categories = Category.objects.all()
    category = Category.objects.filter(slug=slug).first()

    news_posts = Post.objects.filter(category__title='Новини').all()
    manuals_posts = Post.objects.filter(category__title='Мануали').all()

    posts_list = Post.objects.filter(category=category)


    page = request.GET.get('page', 1)
    paginator = Paginator(posts_list, 10)

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    context={
        'tags': tags,
        'posts': posts, 
        'news_posts': news_posts,
        'manuals_posts': manuals_posts,
        'category': category, 
        'categories': categories
    }
    return render(request, 'category-page.html', context=context)

def post_page(request, slug):
    tags = Tags.objects.all()
    post = Post.objects.filter(slug=slug).first()
    categories = Category.objects.all()
    post_tags = post.tags.all()

    news_posts = Post.objects.filter(category__title='Новини').all()
    manuals_posts = Post.objects.filter(category__title='Мануали').all()
    


    context = {
        'tags': tags,
        'post': post, 
        'news_posts': news_posts,
        'manuals_posts': manuals_posts,
        'categories': categories, 
        'post_tags': post_tags 
    }
    return render(request, 'post-page.html', context=context)

def tag_page(request, slug):
    tags = Tags.objects.all()
    tag = Tags.objects.filter(slug=slug).first()
    categories = Category.objects.all()

    news_posts = Post.objects.filter(category__title='Новини').all()
    manuals_posts = Post.objects.filter(category__title='Мануали').all()

    posts_list = tag.post_set.all()

    page = request.GET.get('page', 1)
    paginator = Paginator(posts_list, 10)

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)


    context= {
        'tags': tags,
        'tag': tag,
        'posts': posts,
        'news_posts': news_posts,
        'manuals_posts': manuals_posts,
        'categories': categories
    }
    return render(request, 'tag-page.html', context=context)


class SearchView(ListView):
    model = Post
    template_name = 'search_results.html'
    # context_object_name = 'context'


    def get_queryset(self): # new
        query = self.request.GET.get('q')
        objects = Post.objects.filter(
            Q(title__icontains=query)
        )
        page = self.request.GET.get('page', 1)
        paginator = Paginator(objects, 10)

        try:
            object_list = paginator.page(page)
        except PageNotAnInteger:
            object_list = paginator.page(1)
        except EmptyPage:
            object_list = paginator.page(paginator.num_pages)


        return object_list
    
    def get_context_data(self, **kwargs):
        context = super(ListView, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


def contacts(request):
    context= {
        'categories': Category.objects.all()
    }
    return render(request, 'contacts-page.html', context=context)

def about(request):
    context= {
        'categories': Category.objects.all()
    }
    return render(request, 'about-page.html', context=context)

def privacy(request):
    context= {
        'categories': Category.objects.all()
    }
    return render(request, 'privacy-page.html', context=context)

def custom_page_not_found_view(request, exception):
    return render(request, "errors/404.html", {})

def custom_error_view(request, exception=None):
    return render(request, "errors/500.html", {})

def custom_permission_denied_view(request, exception=None):
    return render(request, "errors/403.html", {})

def custom_bad_request_view(request, exception=None):
    return render(request, "errors/400.html", {})