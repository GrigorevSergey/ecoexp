from django.urls import path
from .views import post_form, home


urlpatterns = [
    path('', home, name='home'),
    path('post_form', post_form, name='post_form'),


]