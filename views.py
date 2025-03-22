from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, "home.html")

@login_required(login_url='login')
def about(request):
    return render(request, 'about.html')

def login_view(request):
    if request.user.is_authenticated:
        messages.info(request, "You are already logged in. Logout to switch accounts.")
        return redirect('portfolio')

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")  # Redirecting to home page after login
        else:
            return render(request, "login.html", {"error": "Invalid username or password"})
    
    return render(request, "login.html")

def register_view(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 != password2:
            messages.error(request, "Passwords do not match.")
        elif User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken.")
        elif User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered.")
        else:
            user = User.objects.create_user(username=username, email=email, password=password1)
            user.save()
            messages.success(request, "Account created successfully! Please log in.")
            return redirect('login')

    return render(request, "register.html")

def logout_view(request):
    logout(request)
    return redirect('home')  # Redirect to home page after logout

@login_required
def portfolio_view(request):
    return render(request, "portfolio.html")
