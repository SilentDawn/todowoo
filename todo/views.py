from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.shortcuts import redirect, render

# Create your views here.

def home(request):
	return render(request, 'todo/home.html')

def signup_user(request):
	if request.method == 'GET':
		return render(request, 'todo/signup_user.html', {'form':UserCreationForm()})
	else:
		if request.POST['password1'] == request.POST['password2']:
			try:
				user = User.objects.create_user(request.POST['username'].lower(), password=request.POST['password1'])
				user.save()
				login(request, user)
				return redirect('current_todos')

			except IntegrityError:
				return render(request, 'todo/signup_user.html', {'form':UserCreationForm(), 'error':'Username not available'})	
		else:
			return render(request, 'todo/signup_user.html', {'form':UserCreationForm(), 'error':'Passwords did not match'})

def login_user(request):
	if request.method == 'GET':
		return render(request, 'todo/login_user.html', {'form':AuthenticationForm()})
	else:
		user = authenticate(request, username = request.POST['username'].lower(), password = request.POST['password'])
		if user is None:
			return render(request, 'todo/login_user.html', {'form':AuthenticationForm(), 'error':'Invalid username/password'})
		login(request, user)
		return redirect('current_todos')
	
def logout_user(request):
	if request.method == 'POST':
		logout(request)
		return redirect('home')

def current_todos(request):
	return render(request, 'todo/current_todos.html')