from django.urls import path
from app_site import views

urlpatterns = [
    path('', views.home),
    path('sobre/', views.sobre),
]