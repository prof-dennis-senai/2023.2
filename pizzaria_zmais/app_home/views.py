from django.shortcuts import render, redirect
from app_home.models import PizzaModel, VendaPizzaModel, VendaModel, ClienteModel
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    pesquisa = request.GET.get('busca')
    if pesquisa:
        lista_produtos = PizzaModel.objects.filter(pizza__icontains=pesquisa)
    else:
        lista_produtos = PizzaModel.objects.all()
    return render(request, 'app_home/pages/home.html', context={'produtos': lista_produtos, 'pesquisa': pesquisa})


@login_required
def criar_pizza(request):
    if request.method == 'GET':
        return render(request, 'app_home/pages/pizza.html')
    
    pizza = request.POST.get('pizza')
    preco = request.POST.get('preco')
    imagem = request.POST.get('imagem')
    ingredientes = request.POST.get('ingredientes')
    pizza = PizzaModel.objects.create(pizza=pizza, preco=preco, imagem=imagem, ingredientes=ingredientes)
    return render(request, 'app_home/pages/pizza.html', context={'pizza': pizza})

@login_required
def listar_pizzas(request):
    pizzas = PizzaModel.objects.all()
    return render(request, 'app_home/pages/listar.html', context={'pizzas': pizzas})

@login_required
def deletar_pizza(request, id):
    pizza = PizzaModel.objects.get(id=id)
    pizza.delete()
    return redirect('listar') 

@login_required
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

def mandar_email(usuario,mensagem,titulo):
    print(f'Enviando email para {usuario} com a mensagem: {mensagem}')
    send_mail(
    titulo,
    mensagem,
    'seu_email@gmail.com',
    [usuario],
    fail_silently=False,
)

@login_required
def venda_pizza(request):
    vendas_raw = VendaPizzaModel.objects.select_related('venda', 'pizza').order_by('venda__id')

    vendas = []
    ultima_id = None
    cor_atual = '#ff0000'

    for item in vendas_raw:
        if item.venda.id != ultima_id:
            cor_atual = '#00ff00' if cor_atual == '#ff0000' else '#ff0000'
            ultima_id = item.venda.id
        vendas.append({
            'venda': item.venda,
            'pizza': item.pizza,
            'cor': cor_atual
        })

    return render(request, 'app_home/pages/venda_pizza.html', context={'vendas': vendas})

    """
    # O que o Django faz com o select_related
    SELECT *
    FROM tabela1
    INNER JOIN tabela2 
    ON tabela1.id = tabela2.id
    

    # O que o Django faz sem o select_related
    SELECT *
    FROM tabela1

    SELECT campo
    FROM tabela2
    WHERE id = x
    """

def cadastrar_cliente(request):
    if request.method == 'GET':
        return render(request, 'app_home/pages/cadastrar_cliente.html')
    
    nome = request.POST.get('nome')
    endereco = request.POST.get('endereco')
    email = request.POST.get('email')
    ClienteModel.objects.create(nome=nome, endereco=endereco, email=email)
    return redirect(cadastrar_cliente)