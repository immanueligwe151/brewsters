from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, EmailLoginForm
from .models import Category

# Welcome view
def welcome(request):
    if request.user.is_authenticated:
        return redirect('home')  # Redirect to home if the user is logged in
    return render(request, 'brewsters_app/welcome.html')

# Login view
def login_view(request):
    if request.method == 'POST':
        form = EmailLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, username=email, password=password)  # Using email as the username
            if user is not None:
                login(request, user)  # Log the user in
                return redirect('home')  # Redirect to home after successful login
            else:
                messages.error(request, 'Invalid email or password')
    else:
        form = EmailLoginForm()

    return render(request, 'brewsters_app/login.html', {'form': form})

# Sign up view
def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the user
            # Automatically log in the user
            username = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(request, username=username, password=raw_password)
            if user is not None:
                login(request, user)  # Log in the user
            return redirect('home')  # Redirect to the home page after login
    else:
        form = CustomUserCreationForm()

    return render(request, 'brewsters_app/signup.html', {'form': form})

# Logout view
def logout_view(request):
    logout(request)
    return redirect('welcome')  # Redirect to welcome page after logging out

# Home view
#@login_required  # Ensure the user is logged in to access this view
def home_view(request):
    if not request.user.is_authenticated:
        return redirect('welcome')  # Redirect to home if the user is logged in
    categories = Category.objects.all()  # Query to get all items from the database
    return render(request, 'brewsters_app/home.html', {'categories': categories})