from django.shortcuts import render, redirect
from app_home.models import PizzaModel

# Create your views here.
def home(request):
    print(request.session.get('pizza', []), request.session.get('quantidade_pizzas', 0))
    lista_produtos = PizzaModel.objects.all()
    return render(request, 'app_home/pages/home.html', context={'produtos': lista_produtos, })


def criar_pizza(request):
    if request.method == 'GET':
        return render(request, 'app_home/pages/pizza.html')
    
    pizza = request.POST.get('pizza')
    preco = request.POST.get('preco')
    imagem = request.POST.get('imagem')
    ingredientes = request.POST.get('ingredientes')
    PizzaModel.objects.create(pizza=pizza, preco=preco, imagem=imagem, ingredientes=ingredientes)
    return render(request, 'app_home/pages/pizza.html', context={'pizza': pizza})


def listar_pizzas(request):
    pizzas = PizzaModel.objects.all()
    return render(request, 'app_home/pages/listar.html', context={'pizzas': pizzas})


def deletar_pizza(request, id):
    pizza = PizzaModel.objects.get(id=id)
    pizza.delete()
    return redirect('listar') 


def atualizar_pizza(request, id):
    if request.method == 'GET':
        pizza = PizzaModel.objects.get(id=id)
        return render(request, 'app_home/pages/atualizar_pizza.html', context={'pizza': pizza})
    
    pizza = request.POST.get('pizza')
    preco = request.POST.get('preco')
    imagem = request.POST.get('imagem')
    ingredientes = request.POST.get('ingredientes')
    PizzaModel.objects.filter(id=id).update(pizza=pizza, preco=preco, imagem=imagem, ingredientes=ingredientes)
    return redirect('listar')

def carrinho_pizza(request, id):
    pizzas = request.session.get('pizza', [])
    pizzas.append(id)
    request.session['pizza'] = pizzas

    quantidade_pizzas = request.session.get('quantidade_pizzas', 0)
    quantidade_pizzas = len(pizzas)
    request.session['quantidade_pizzas'] = quantidade_pizzas
    return redirect('home')

def comprar_carrinho_pizza(request):
    pizzas = request.session.get('pizza', [])
    lista_pizzas = []
    for pizza in pizzas:
        pizza = PizzaModel.objects.get(id=pizza)
        lista_pizzas.append(pizza)
    
    return render(request, 'app_home/pages/listar_carrinho.html', context={'pizzas': lista_pizzas, 'quantidade_pizzas': len(pizzas)})