from django.shortcuts import render, redirect
from app_home.models import PizzaModel, VendaPizzaModel, VendaModel

def carrinho_pizza(request, id):
    pizzas = request.session.get('pizza', [])
    pizzas.append(id)
    request.session['pizza'] = pizzas

    quantidade_pizzas = request.session.get('quantidade_pizzas', 0)
    quantidade_pizzas = len(pizzas)
    request.session['quantidade_pizzas'] = quantidade_pizzas
    return redirect('home')

def limpar_carrinho_pizza(request):
    request.session['pizza'] = []
    request.session['quantidade_pizzas'] = 0
    return redirect('home')

def comprar_carrinho_pizza(request):
    pizzas = request.session.get('pizza', [])
    lista_pizzas = []
    for pizza in pizzas:
        pizza = PizzaModel.objects.get(id=pizza)
        lista_pizzas.append(pizza)
    
    return render(request, 'app_home/pages/listar_carrinho.html', context={'pizzas': lista_pizzas, 'quantidade_pizzas': len(pizzas)})

def finalizar_carrinho_pizza(request):
    pizzas = request.session.get('pizza', [])
    if not pizzas:
        return redirect('comprar_carrinho_pizza')

    pizzas = PizzaModel.objects.filter(id__in=pizzas)

    venda = VendaModel.objects.create()

    for pizza in pizzas:
        VendaPizzaModel.objects.create(pizza=pizza, venda=venda, preco=pizza.preco)

    request.session['pizza'] = []
    request.session['quantidade_pizzas'] = 0
    return render(request, 'app_home/pages/finalizar_carrinho.html', context={'pizzas': pizzas})
