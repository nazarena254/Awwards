from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest,Http404,HttpResponse,HttpResponseRedirect
from .models import Profile, Project, Rate
from .email import send_welcome_email
from .forms import *

# Create your views here.
def signup_view(request):
    if request.method=="POST":
        form=SignUpForm(request.POST)
        if form.is_valid:
            form.save()
            #cleaned_data.get()-Any data user submits thru form will be passed to server as strings
            username=form.cleaned_data.get("username")
            password=form.cleaned_data.get("password1")
            name=form.cleaned_data['username']
            email=form.cleaned_data['email']
            send_welcome_email(name, email)
            user=authenticate(username=username, password=password)
            login(request,user)
            return redirect('welcome')
        else:
            form=SignUpForm()
        return render(request, 'registration/signup', {"form":form})     
