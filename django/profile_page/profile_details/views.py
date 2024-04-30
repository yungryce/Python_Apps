from django.shortcuts import render
from django.views.generic import CreateView
from .models import Profile
from .forms import ProfileForm

class ProfileView(CreateView):
    model = Profile
    template_name = 'profile_details/home.html'
    # fields = '__all__'
    form_class = ProfileForm