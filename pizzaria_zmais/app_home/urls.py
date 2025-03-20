from django.urls import path
from app_home import views

urlpatterns = [
    path('', views.home, name='home'),
    path('pizza/', views.criar_pizza, name='pizza'),
]
