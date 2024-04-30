from django.urls import path
# from . import views
from .views import DetailV, Homeview, CreateFormView, UpdateFormView, DeleteFormView, AddCategoryView

# app_name = 'blog' not working when name added to path

urlpatterns = [
    # path('', views.index, name='index'),
    path('', Homeview.as_view(), name='home'),
    path('<int:pk>/', DetailV.as_view(), name='details'),
    path('forms', CreateFormView.as_view(), name='createform'),
    path('forms/<int:pk>/', UpdateFormView.as_view(), name='updateform'),
    path('forms/<int:pk>/deletepost', DeleteFormView.as_view(), name='deletepost'),
    path('category', AddCategoryView.as_view(), name='category'),

]
