from django.contrib import admin

from .models import Produto

admin.site.register(Produto)

class ProdutoAdmin(admin.ModelAdmin):
    list_dispaly = ('nome', 'descricao', 'preco', 'url_imagem')
