from django.urls import path
from app_home import views

urlpatterns = [
    path('', views.home, name='home'),
    path('pizza/', views.criar_pizza, name='pizza'),
    path('listar/', views.listar_pizzas, name='listar'),
    path('deletar/<int:id>', views.deletar_pizza, name='deletar'),
    path('atualizar/<int:id>', views.atualizar_pizza, name='atualizar'),
]
