from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def register(request):
	form = UserCreationForm()
	context = {
		'form':form,
		'title': 'Sign Up'
	}
	return render(request, 'account/register.html', context)
