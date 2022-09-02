from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('<str:usern>/',views.HomeView.as_view(),name='profile'),
]
