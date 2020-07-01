from django.contrib.auth 			import login
from django.contrib.auth.forms 		import UserCreationForm
from django.contrib.auth.models 	import User
from django.db 						import IntegrityError
from django.shortcuts 				import render, redirect

# Create your views here.

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
	
def current_todos(request):
	return render(request, 'todo/current_todos.html')