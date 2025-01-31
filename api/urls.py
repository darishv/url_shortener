from django.urls import path
from . import views

urlpatterns = [
    path('', views.shorten_url, name='url_shortener'),  # POST to generate shortened URL
    path('<str:shortened_url>/', views.redirect_to_long_url, name='url_redirect'),  # GET to redirect
]