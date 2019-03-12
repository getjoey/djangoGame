# accounts/urls.py
from django.urls import path

from . import views

app_name = 'play' #this is namespacing

urlpatterns = [
    path('', views.play, name='play'),
    path('update/', views.update, name='update'),
]