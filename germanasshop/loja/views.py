from django.shortcuts import get_object_or_404, render
from cliente.models import Cliente
from .models import Produto

# Create your views here.
def index(request): 
    produtos = Produto.objects.all()
    context = {'produtos':produtos}
    return render(request, 'loja/index.html', context)

def login(request):
    return render(request, 'loja/Inicial.html')

def forum(request):
    return render(request, 'loja/forum.html')

def cesta(request):
    return render(request, 'loja/cesta.html')

def produto(request, id_produto):
    produto = get_object_or_404(Produto, pk=id_produto)
    context = {}
    context['produto'] = produto
    return render(request, 'loja/produto.html', context)