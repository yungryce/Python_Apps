from django.shortcuts import render
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from .models import Reg, Category
from .forms import Postform, Editform
from django.urls import reverse_lazy 

# Create your views here.
# def index(request):
#     return render(request, 'blog_codemy/index.html')

class Homeview(ListView):
    model = Reg
    template_name = 'blog/home.html'
    ordering = '-pub_date'


class DetailV(DetailView):
    model = Reg
    template_name = 'blog/art_det.html'

class CreateFormView(CreateView):
    model = Reg
    template_name = 'blog/createform.html'
    # cant use fields with form_class as fields is defined in form_class
    form_class = Postform
    # fields = '__all__'
    # fields = ('title', 'body')


class UpdateFormView(UpdateView):
    model = Reg
    template_name = 'blog/updateform.html'
    form_class = Editform
    # fields = '__all__'
    # fields = ('title', 'title_tag','body') 

    

class DeleteFormView(DeleteView):
    model = Reg
    template_name = 'blog/deleteform.html'
    success_url = reverse_lazy('home')



class AddCategoryView(CreateView):
    model = Category
    template_name = 'blog/Categoryform.html'
    fields = "__all__"