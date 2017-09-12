from django.contrib.syndication.views import Feed

from .models import Post

class AllPostsRSSFeed(Feed):
	title = "Django RSS Demo"

	link = "/"

	description = "Test Text for RSS"

	def items(self):
		return Post.objects.all()

	def item_title(self, item):
		return '[%s] %s' %(item.category, item.title)

	def item_description(self, item):
		return item.body