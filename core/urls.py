from django.urls import path

from . import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('posts/<slug:slug>', views.category_page, name='category_page')
]
