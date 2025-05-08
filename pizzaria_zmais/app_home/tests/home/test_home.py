import pytest

from django.test import Client
from django.urls import reverse

from app_home.models import PizzaModel

# Create your tests here.
def test_url_home():
    url = reverse('home')
    assert url == '/'

@pytest.mark.django_db
def test_url_home_200():
    client = Client()
    response = client.get(reverse('home'))
    assert response.status_code == 200

@pytest.mark.django_db
def test_url_home_200_empty():
    client = Client()
    response = client.get(reverse('home'))
    assert "A página ainda não possui produtos" in response.content.decode('utf-8')

@pytest.mark.django_db
def test_url_home_200_not_empty():
    PizzaModel.objects.create(
        pizza='Mussarela', 
        preco=15.00,
        imagem='https://zermattpizza.com.br/imgs/produto-pizza-sabor-mussarela-pizzaria-delivery-florianopolis-sao-jose.png',
        ingredientes='Queijo mussarela'
    )
    client = Client()
    response = client.get(reverse('home'))
    
    assert "/carrinho/1" in response.content.decode('utf-8')
    assert "Mussarela" in response.content.decode('utf-8')
    assert "R$15.00" in response.content.decode('utf-8')
    assert "https://zermattpizza.com.br/imgs/produto-pizza-sabor-mussarela-pizzaria-delivery-florianopolis-sao-jose.png" in response.content.decode('utf-8')
    assert "Queijo mussarela" in response.content.decode('utf-8')