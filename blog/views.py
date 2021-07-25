from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from .forms import ContentFieldForm

# Create your views here.

def home(request):
	context = {}
	context['posts'] = Post.objects.all().order_by('-date_posted')
	context['title'] = "Home"
	return render(request, "blog/home.html", context)

def blogDetail(request, pk):
	context = {}
	post = Post.objects.get(pk=pk)
	content = ContentFieldForm(instance=post)
	context['post'] = post
	context['content'] = content
	context['title'] = '{}'.format(post.title) 
	context['isEditable'] = (post.author == request.user)
	return render(request, "blog/detail.html", context)

def about(request):
	context = {}
	context['title'] = "About"
	return render(request, "blog/about.html", context)
	