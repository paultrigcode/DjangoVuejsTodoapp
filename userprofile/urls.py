from django.contrib import admin
from django.urls import path,include
from .views import user_create,signup,UserView

urlpatterns = [
    path('create/',user_create,name='home'),
    path('signup/',signup,name='signup'),
    path('',UserView.as_view(),name='user-create'),



]