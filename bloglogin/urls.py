from django.contrib import admin
from django.urls import path, include
from .views import UserRegisterView
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
]
