# accounts/urls.py
from django.urls import path

from . import views

app_name = 'characterinfo' #this is namespacing

urlpatterns = [
    path('info/', views.info, name='info'),
    path('createcharacter/', views.createcharacter, name='createcharacter'),
    path('create/', views.create, name='create'),
]