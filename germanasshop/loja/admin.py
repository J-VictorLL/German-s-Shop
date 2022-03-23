from django.contrib import admin

from .models import Reclamacao, Produto

admin.site.register(Produto)
admin.site.register(Reclamacao)

class ProdutoAdmin(admin.ModelAdmin):
    list_dispaly = ('nome', 'descricao', 'preco', 'url_imagem')
