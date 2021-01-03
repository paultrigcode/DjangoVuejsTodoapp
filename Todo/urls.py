from django.contrib import admin
from django.urls import path,include
from .views import home, TodoView,markComplete,delete

urlpatterns = [
    path('home/',home,name='home'),
    path('',TodoView.as_view(),name='todo-create'),
	path('<int:id>/complete/',markComplete,name="todo-complete"),	
	path('<int:id>/delete/',delete,name="todo-delete"),

]
