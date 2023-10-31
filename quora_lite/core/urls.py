# core/urls.py

from django.urls import path
from .views import QuestionCreateView, answer_create_view
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render, redirect
from .views import registration_view , login_view , logout_view


urlpatterns = [
    path('ask/', QuestionCreateView.as_view(), name='question_create'),
    path('question/<int:pk>/answer/', answer_create_view, name='answer_create'),
    path('register/', registration_view, name='registration'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('admin/', admin.site.urls),
    # Include Django's built-in authentication views
    path('accounts/', include('django.contrib.auth.urls')),
]
def logout_view(request):
    logout(request)
    return redirect('home')  # Redirect to the home page after logout
path('logout/', logout_view, name='logout'),

from django.contrib.auth import views as auth_views

urlpatterns = [
    # ... your other URL patterns ...
    path('accounts/', include('django.contrib.auth.urls')),
]

