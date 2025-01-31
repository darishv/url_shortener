from django.urls import path
from . import views

urlpatterns = [
    path('', views.url_shortener, name='get_url_shortener'),
]