from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from .forms import CandidateForm

# Create your views here.

def homeview(request):
    if request.method == 'POST':
        form = CandidateForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'successful')
            return HttpResponseRedirect('/home/')
    else:
        form = CandidateForm()
    return render(request, 'inputs/home.html', {'form':form})
