from django.shortcuts import render

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
    return render(request, 'app_home/pages/home.html', context={'produtos': lista_produtos})


def criar_pizza(request):
    return render(request, 'app_home/pages/pizza.html')