from django.shortcuts import render, redirect
# from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .forms import LoginForm, SignUpForm
from django.contrib import messages
from django.http import HttpResponse


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user.is_authenticated():
                messages.success(request, 'successful')
                return redirect('/user/')
            else:
                messages.error(request, 'please try again or signup')
        else:
            messages.warning(request, 'please validate form')
    else:
        form = LoginForm()
    return render(request, 'inputs/home.html', {'form':form})


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)
            messages.success(request, 'successful')
            return HttpResponseRedirect('/home/')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form':form})