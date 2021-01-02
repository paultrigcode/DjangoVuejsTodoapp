from django.contrib import admin
from django.urls import path,include
from .views import home, TodoView

urlpatterns = [
    path('home/',home,name='home'),
    path('',TodoView.as_view(),name='todo-create')


]
