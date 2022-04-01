from django.contrib import admin

from .models import Reclamacao, Produto,Carrinho

admin.site.register(Produto)
admin.site.register(Reclamacao)
admin.site.register(Carrinho)
