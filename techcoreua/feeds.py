from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords

from core.models import Post

class LatestPostsFeed(Feed):
    title = 'techcoreua'
    link = ''
    description = 'Нові дописи на порталі'

    def items(self):
        return Post.objects.all()

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.preview_text

