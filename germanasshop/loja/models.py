from datetime import datetime
from django.db import models

from cliente.models import Usuario

class Produto(models.Model):
    nome = models.CharField('Nome', max_length=100)
    preco = models.DecimalField('Preço', max_digits=7, decimal_places=2)
    descricao = models.TextField('Descrição')
    url_imagem = models.URLField('Url Imagem')
    categoria = models.CharField('Categoria', max_length=50)

    def __str__(self):
        return str(self.pk) + ' ' + self.nome

class Reclamacao(models.Model):
    titulo = models.CharField('Título', max_length=100)
    reclamação = models.TextField('Reclamação')
    resposta = models.TextField('Resposta', null=True)
    data_pergunta = models.DateTimeField('Data Pergunta', default=datetime.now())
    data_resposta = models.DateTimeField('Data Resposta', null=True)

    def __str__(self):
        return str(self.pk) + ' ' + self.titulo

class Favorito(models.Model):
    id_usuario = models.ForeignKey(Usuario, on_delete = models.CASCADE)
    id_produto = models.ForeignKey(Produto, on_delete = models.CASCADE)
    data_adicao = models.DateTimeField('Data da Adição na lista',default=datetime.now())
    #Como juntar as duas chaves pra não haver repetição