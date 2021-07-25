from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegistrationForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from blog.models import Post
from django.contrib.auth.models import User

# Create your views here.

def register(request):
	if request.method == "POST":
		form = UserRegistrationForm(request.POST)
		# if form is valid redirect to home url with success message
		if form.is_valid():
			new_user = form.save()
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
	context = {}
	current_logged_user = request.user

	if request.GET:
		getuser = User.objects.get(pk=request.GET['uid'])
		posts = Post.objects.filter(author=getuser)

		context['title'] = "{}'s profile".format(getuser.username)
		context['posts'] = posts
		context['getuser'] = getuser
		context['post_count'] = posts.count()
		context['isEditable'] = (current_logged_user == getuser)

	return render(request, 'account/profile.html', context)

@login_required
def updateProfile(request):
	context = {}

	if request.method == 'POST':
		user_form = UserUpdateForm(request.POST, instance=request.user)
		profile_form = ProfileUpdateForm(
			request.POST,
			request.FILES,
			instance=request.user.profile)
		if user_form.is_valid() and profile_form.is_valid():
			user_form.save()
			profile_form.save()
			messages.success(request, "Update profile successfully.")
			return redirect('update-profile')
	else:
		user_form = UserUpdateForm(instance=request.user)
		profile_form = ProfileUpdateForm(instance=request.user.profile)

	context['user_form'] = user_form
	context['profile_form'] = profile_form
	context['title'] = 'Update profile'
	
	return render(request, 'account/update.html', context)