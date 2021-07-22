from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegistrationForm
from django.contrib.auth.decorators import login_required
from blog.models import Post
from account.models import Profile

# Create your views here.

def register(request):
	if request.method == "POST":
		form = UserRegistrationForm(request.POST)
		# if form is valid redirect to home url with success message
		if form.is_valid():
			new_user = form.save()
			profile = Profile(user=new_user)
			profile.save()
			login(request, new_user)
			username = form.cleaned_data.get('username')
			messages.success(request, "Welcome {}".format(username))
			return redirect('blog-home')
	else:
		form = UserRegistrationForm()
	context = {
		'form':form,
		'title': 'Sign Up',
	}
	return render(request, 'account/register.html', context)

def profile(request):
	if request.GET:
		post = Post.objects.filter(author.user.pk==request.GET['uid'])
	return render(request, 'account/profile.html')