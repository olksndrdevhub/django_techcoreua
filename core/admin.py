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
    list_display = ('id', 'title', 'draft', 'creating_date', 'category', 'star')
    actions = ['publish', 'unpablish', 'star', 'unstar']

    search_fields = ['title', 'preview_text']
    list_filter = ['star', 'draft', 'category', 'creating_date']



    def publish(self, request, queryset):
        queryset.update(draft=False)
    publish.short_description = "Опублікувати обрані пости"

    def unpablish(self, request, queryset):
        queryset.update(draft=True)
    unpablish.short_description = 'Приховати обрані пости'

    def unstar(self, request, queryset):
        queryset.update(star=False)
    unstar.short_description = 'Видалити з топ-постів'

    def star(self, request, queryset):
        queryset.update(star=True)
    star.short_description = 'Додати до топ-постів'
    


# Default FileBrowser site
site = FileBrowserSite(name='filebrowser', storage=DefaultStorage())


admin.site.register(Category)
admin.site.register(Post, PostAdmin)
admin.site.register(Tags)