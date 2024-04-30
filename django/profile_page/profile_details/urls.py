from django.urls import path
from .views import ProfileView
# from . import views

urlpatterns = [
    path('', ProfileView.as_view(), name='user'),
    # path('', views.ProfileView, name='user'),
]
