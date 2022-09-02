from http.client import HTTPResponse
from django.shortcuts import render
from blogcrud import models
from django.views.generic import ListView
# Create your views here.
# def profile(request,usern):
#     return render(request,'userprofile.html')

class HomeView(ListView):
    model = models.Post
    template_name = 'userprofile.html'
    ordering = ['-post_date']
 