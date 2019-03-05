from django.urls import path

from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('get_argument',views.test_get_argument),
    path('if_tag',views.if_tag),
    path('for_in_tag',views.for_in_tag),
    path('get_input_test',views.get_input_test),
    path('get_input_value',views.get_post_value),
    path('study_redirect',views.study_redirect),
]