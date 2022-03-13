import datetime
import email
from django.db import models
from django.utils import timezone



# class Question(models.Model):
#     question_text = models.CharField('Questão',max_length=200)
#     pub_date = models.DateTimeField('Data de publicação')

#     def __str__(self):
#         return self.question_text

#     def was_published_recently(self):
#         return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)

#     def __str__(self):
#         return self.choice_text

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=200, unique=True)
    cpf = models.CharField(max_length=11,primary_key=True)
    senha = models.CharField(max_length=50)

    def __str__(self):
        return self.nome
