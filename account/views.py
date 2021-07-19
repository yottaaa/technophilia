from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegistrationForm

# Create your views here.

def register(request):
	if request.method == "POST":
		form = UserRegistrationForm(request.POST)
		# if form is valid redirect to home url with success message
		if form.is_valid():
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
