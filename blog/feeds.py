from django.contrib.syndication.views import Feed
from .models import Post

# RSS订阅
class AllPostsRssFeed(Feed):
    title = 'Django_blog'
    link = '/'
    description = 'Django_blog Python'

    def items(self):
        return Post.objects.all()

    def item_title(self, item):
        return '[{}] {}'.format(item.category, item.title)

    def item_description(self, item):
        return item.body