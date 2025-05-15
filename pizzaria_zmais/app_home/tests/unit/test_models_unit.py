import pytest
from app_home.models import PizzaModel, VendaModel, VendaPizzaModel

@pytest.fixture
def venda_pizza_function():
    pizza = PizzaModel.objects.create(
        pizza='Mussarela', 
        preco=15.00,
        imagem='https://zermattpizza.com.br/imgs/produto-pizza-sabor-mussarela-pizzaria-delivery-florianopolis-sao-jose.png',
        ingredientes='Queijo mussarela'
    )

    pizza_venda1 = VendaModel.objects.create()
    VendaPizzaModel.objects.create(
        pizza=pizza, 
        venda=pizza_venda1,
        preco=15.00
    )

    pizza_venda2 = VendaModel.objects.create()
    VendaPizzaModel.objects.create(
        pizza=pizza, 
        venda=pizza_venda2,
        preco=15.00
    )

@pytest.mark.django_db
def test_quantidade_de_compra_por_usuario(venda_pizza_function):
    
    qtd_pizzas = VendaPizzaModel.quantidade_vendida('Mussarela')
    assert qtd_pizzas == 2
    

