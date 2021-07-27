from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from .models import Post
from .forms import BlogForm

# Create your views here.

def home(request):
	context = {}
	context['posts'] = Post.objects.all().order_by('-date_posted')
	context['title'] = "Home"
	return render(request, "blog/home.html", context)

def blogDetail(request, pk):
	context = {}
	post = Post.objects.get(pk=pk)
	context['post'] = post
	context['title'] = '{}'.format(post.title) 
	context['isEditable'] = (post.author == request.user)
	return render(request, "blog/detail.html", context)

@login_required
def blogCreate(request):
	context = {}

	if request.method == 'POST':
		blog_form = BlogForm(request.POST)
		if blog_form.is_valid():
			blog_form.instance.author = request.user
			blog_form.save()
			messages.success(request, "Create new blog successfully.")
			return redirect('blog-home')
	else:
		blog_form = BlogForm()
		context['blog_form'] = blog_form

	context['title'] = "Add new blog"
	return render(request, "blog/create.html", context)

@login_required
def blogEdit(request, pk):
	context = {}
	blog = Post.objects.get(pk=pk,author=request.user)
	if request.method == 'POST':
		blog_form = BlogForm(request.POST)
		if blog_form.is_valid():
			blog_form.instance.author = request.user
			blog_form.save()
			messages.success(request, "Update blog successfully.")
			return redirect('blog-home')
	else:
		blog_form = BlogForm(instance=blog)
		context['blog_form'] = blog_form

	context['title'] = "Add new blog"
	return render(request, "blog/create.html", context)

def about(request):
	context = {}
	context['title'] = "About"
	return render(request, "blog/about.html", context)
	