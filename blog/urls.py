from django.urls import path

from . import views
urlpatterns = [
    path('login',views.login),
    path('index',views.index),
    path('get_valid_img',views.get_valid_img),
    path('register',views.register),
]
