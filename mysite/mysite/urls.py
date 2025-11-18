from django.contrib import admin
from django.urls import path
import mlapp.views

urlpatterns = [
    path('', mlapp.views.home, name='home'),
    path('about/', mlapp.views.about, name='about'),
    path('myui/', mlapp.views.myui, name='myui'),
    path('myapi/', mlapp.views.myapi, name='myapi'),
    path('ourteam/', mlapp.views.ourteam, name='ourteam'),
    path('predict/', mlapp.views.predict, name='predict'),  # ✅ name added here
    path('contact/', mlapp.views.contact, name='contact'),
    path('finalresult/', mlapp.views.finalresult, name='finalresult'),
]