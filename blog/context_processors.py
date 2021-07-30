from .models import Post, BlogView

def recommendationContext(request):
	context = {}
	blog_views = BlogView.objects.values('blog').distinct()
	posts = list()

	# Make post datastructure
	for blog in blog_views:
		post = Post.objects.get(pk=blog.get('blog'))
		views = BlogView.objects.filter(blog=post).count()
		posts.append({
			'blog':post,
			'views':views,
		})

	
	posts = sorted(posts, key=lambda e: e['views'], reverse=True)

	context['recommended_posts'] = posts
	return context