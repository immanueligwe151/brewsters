from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

# Welcome view
def welcome(request):
    if request.user.is_authenticated:
        return redirect('home')  # Redirect to home if the user is logged in
    return render(request, 'brewsters_app/welcome.html')

# Login view
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to home view on successful login
        else:
            return render(request, 'brewsters_app/login.html', {'error': 'Invalid credentials'})
    return render(request, 'brewsters_app/login.html')

# Sign up view
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')  # Redirect to home view after signing up
    else:
        form = UserCreationForm()
    return render(request, 'brewsters_app/signup.html', {'form': form})

# Logout view
def logout_view(request):
    logout(request)
    return redirect('welcome')  # Redirect to welcome page after logging out

# Home view
@login_required  # Ensure the user is logged in to access this view
def home_view(request):
    return render(request, 'brewsters_app/home.html')