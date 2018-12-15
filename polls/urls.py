from django.urls import path

from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('get_argument',views.test_get_argument),
    path('if_tag',views.if_tag),
]