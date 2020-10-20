from django.contrib.syndication.views import Feed
from django.utils.feedgenerator import Rss201rev2Feed
from django.template.defaultfilters import truncatewords

from core.models import Post


class ExtendedRSSFeed(Rss201rev2Feed):
    """
    Create a type of RSS feed that has content:encoded elements.
    """
    def root_attributes(self):
        attrs = super(ExtendedRSSFeed, self).root_attributes()
        # Because I'm adding a <content:encoded> field, I first need to declare
        # the content namespace. For more information on how this works, check
        # out: http://validator.w3.org/feed/docs/howto/declare_namespaces.html
        attrs['xmlns:content'] = 'http://purl.org/rss/1.0/modules/content/'
        return attrs
    
    def add_item_elements(self, handler, item):
        super(ExtendedRSSFeed, self).add_item_elements(handler, item)

        # 'content_encoded' is added to the item below, in item_extra_kwargs()
        # It's populated in item_your_custom_field(). Here we're creating
        # the <content:encoded> element and adding it to our feed xml
        if item['content_encoded'] is not None:
            handler.addQuickElement(u'content_encoded', item['content_encoded'])

class LatestPostsFeed(Feed):
    title = 'Дописи на сайті TechCoreUa'
    description = 'Дописи на сайті TechCoreUa'
    link = 'https://techcoreua.tk/'
    feed_type = ExtendedRSSFeed

    def item_extra_kwargs(self, item):
        return {'content_encoded': self.item_content_encoded(item)}


    def items(self):
        return Post.objects.all()

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.preview_text

    def item_pubdate(self, item):
        return item.creating_date
    
    def item_author_name(self):
        return 'Олександр Романюк'

    def item_author_email(self):
        return 'oleksandr.romaniuk.work@gmail.com'

    def item_content_encoded(self, item):
        content = '<![CDATA[ <div><img src="{}" style="width:100%" class="img-fluid"></div>{}]]>'.format(item.main_image.url, item.text)

    
    def item_extra_kwargs(self, item):
        extra = super(LatestPostsFeed, self).item_extra_kwargs(item)
        content = '<![CDATA[ <div><img src="{}" style="width:100%" class="img-fluid"></div>{}]]>'.format(item.main_image.url, item.text)
        extra.update({'content_encoded': content})
        return extra

