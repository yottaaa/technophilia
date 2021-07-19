from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.

def home(request):
	context = {}
	context['posts'] = Post.objects.all()
	context['title'] = "Home"
	return render(request, "blog/index.html", context)

def about(request):
	context = {}
	context['title'] = "About"
	return render(request, "blog/about.html", context)
	