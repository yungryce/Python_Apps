from django.urls import path
from .views import SignupView
# from .views import DetailV, Homeview, CreateFormView, UpdateFormView, DeleteFormView

# app_name = 'blog' not working when name added to path

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
]