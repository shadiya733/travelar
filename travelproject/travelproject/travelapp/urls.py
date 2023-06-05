from django.contrib import admin
from django.urls import path,include
from . import views
app_name='travelapp'
urlpatterns = [

    path('',views.demo,name='demo'),
]