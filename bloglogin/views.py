from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.views import generic
from django.contrib.auth.forms import UserCreationForm 
from django.urls import reverse_lazy
from .forms import conForm
from smtplib import SMTP
import getpass


class UserRegisterView(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')


