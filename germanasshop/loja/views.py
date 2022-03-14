from django.shortcuts import render
from cliente.models import Cliente
# Create your views here.
def index(request): 
    context = {}
    context['clientes'] = Cliente.objects.all()
    return render(request, 'geo/index.html',context)

def login(request):
    return render(request, 'geo/login.html')