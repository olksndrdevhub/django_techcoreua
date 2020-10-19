from django.urls import path

from . import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('category/<slug:slug>/', views.category_page, name='category_page'),
    path('post/<slug:slug>/', views.post_page, name='post_page'),
    path('tag/<slug:slug>/', views.tag_page, name='tag_page'),
    path('search/', views.SearchView.as_view(), name='search_results'),
    path('about', views.about, name='about'),
    path('contacts', views.contacts, name='contacts'),
    path('privacy', views.privacy, name='privacy'),
]
