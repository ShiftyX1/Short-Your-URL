from django.urls import path, include
from urlshortener_app import views


urlpatterns = [
    path('', views.index),
    path('<str:short_url>/', views.short_to_dest_url),
]