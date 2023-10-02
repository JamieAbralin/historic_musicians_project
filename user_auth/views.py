from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth import authenticate, login

def user_login(request):
    return render(request, 'authentication/login.html')

def authenticate_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('user_auth:show_user'))
        else:
            return HttpResponseRedirect(reverse('user_auth:login'))
    else:
        # Handle GET requests (e.g., when user accesses the URL directly)
        return render(request, 'authentication/login.html')

def show_user(request):
    return render(request, 'authentication/user.html', {
        "username": request.user.username,
        # Avoid displaying the password for security reasons
    })
