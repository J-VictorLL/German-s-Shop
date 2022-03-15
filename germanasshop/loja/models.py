from django.db import models

class Produto(models.Model):
    nome = models.CharField('Nome', max_length=100)
    preco = models.DecimalField('Preço', max_digits=7, decimal_places=2)
    descricao = models.TextField('Descrição')
    url_imagem = models.URLField('Url Imagem')

    def __str__(self):
        return str(self.pk) + ' ' + self.nome
