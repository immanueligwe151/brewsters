from django.urls import path
from django.contrib.auth import views as auth_views
from .views import welcome, login_view, signup_view, home_view

urlpatterns = [
    path('', welcome, name='welcome'),
    path('login/', login_view, name='login'),
    path('signup/', signup_view, name='signup'),
    path('home/', home_view, name='home'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]