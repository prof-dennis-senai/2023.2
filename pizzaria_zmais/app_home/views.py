from django.shortcuts import render, redirect
from app_home.models import PizzaModel

# Create your views here.
def home(request):
    lista_produtos = [
        {
            'img': 'https://pizzariazermatt.com.br/imgs/produto-pizza-sabor-quatro-queijos-tele-entrega-florianopolis-sao-jose.png',
            'nome': 'Pizza Calabresa',
            'descricao': 'Mussarela, calabresa e cebola.',
            'preco': 'R$ 39,90'
        },
        {
            'img': 'https://pizzariazermatt.com.br/imgs/produto-pizza-sabor-quatro-queijos-tele-entrega-florianopolis-sao-jose.png',
            'nome': 'Pizza Quatro Queijos',
            'descricao': 'Mussarela, provolone, parmesão e gorgonzola.',
            'preco': 'R$ 39,90'
        },
        {
            'img': 'https://pizzariazermatt.com.br/imgs/produto-pizza-sabor-quatro-queijos-tele-entrega-florianopolis-sao-jose.png',
            'nome': 'Pizza Portuguesa',
            'descricao': 'Mussarela, provolone, tomate, azeitona e cebola.',
            'preco': 'R$ 39,90'
        },
        {
            'img': 'https://pizzariazermatt.com.br/imgs/produto-pizza-sabor-quatro-queijos-tele-entrega-florianopolis-sao-jose.png',
            'nome': 'Pizza Portuguesa',
            'descricao': 'Mussarela, provolone, tomate, azeitona e cebola.',
            'preco': 'R$ 39,90'
        },
        {
            'img': 'https://pizzariazermatt.com.br/imgs/produto-pizza-sabor-quatro-queijos-tele-entrega-florianopolis-sao-jose.png',
            'nome': 'Pizza Portuguesa',
            'descricao': 'Mussarela, provolone, tomate, azeitona e cebola.',
            'preco': 'R$ 39,90'
        }
    ]

    lista_produtos = PizzaModel.objects.all()
    return render(request, 'app_home/pages/home.html', context={'produtos': lista_produtos})


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
    pizza = PizzaModel.objects.get(id=id)
    return render(request, 'app_home/pages/pizza.html', context={'pizza': pizza})