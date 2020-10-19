from django.contrib import admin
from django import forms

from ckeditor_uploader.widgets import CKEditorUploadingWidget
from ckeditor.widgets import CKEditorWidget


from django.core.files.storage import DefaultStorage
from filebrowser.sites import FileBrowserSite, site


# Register your models here.
from .models import Category, Post, Tags



class PostAdminForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = Post
        fields = '__all__'

class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm
    list_display = ('id', 'title', 'star', 'creating_date', 'category',)
    


# Default FileBrowser site
site = FileBrowserSite(name='filebrowser', storage=DefaultStorage())


admin.site.register(Category)
admin.site.register(Post, PostAdmin)
admin.site.register(Tags)