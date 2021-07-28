from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from .models import Post, BlogView
from .forms import BlogForm
from django.core.paginator import Paginator

# Create your views here.

def home(request):
	context = {}
	posts = Post.objects.all().order_by('-date_posted')
	paginator = Paginator(posts, 5)
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)

	context['posts'] = page_obj
	context['title'] = "Home"
	return render(request, "blog/home.html", context)

def blogDetail(request, pk):
	context = {}
	post = Post.objects.get(pk=pk)
	blog_views = BlogView.objects.all()

	if not blog_views.filter(blog=post,viewer=request.user).exists():
		BlogView.objects.create(blog=post,viewer=request.user)

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
			if not Post.objects.filter(title=blog_form.instance.title).exists():
				blog_form.instance.author = request.user
				blog_form.save()
				messages.success(request, "Create new blog successfully.")
				return redirect('blog-home')
			else:
				messages.warning(request, "Title \"{}\" are existed.".format(blog_form.instance.title))
			
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

@login_required
def blogDelete(request, pk):
	context = {}
	blog = Post.objects.get(pk=pk,author=request.user)

	if request.method == 'POST':
		if request.POST['blog_id'] == str(blog.id):
			print("Its time to delete")
			blog.delete()
			messages.success(request, "Delete blog successfully.")
			return redirect('blog-home')
	else:
		context['blog'] = blog

	context['title'] = "Delete \"{}\" ".format(blog.title)
	return render(request, "blog/delete.html", context)

def about(request):
	context = {}
	context['title'] = "About"
	return render(request, "blog/about.html", context)
	