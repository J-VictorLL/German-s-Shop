from django.contrib import admin

from .models import Favorito,Reclamacao, Produto

admin.site.register(Produto)
admin.site.register(Reclamacao)
admin.site.register(Favorito)

class ProdutoAdmin(admin.ModelAdmin):
    list_dispaly = ('nome', 'descricao', 'preco', 'url_imagem')
