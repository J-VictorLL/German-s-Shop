from django.contrib import admin

from .models import Question, Choice, Cadastro

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Cadastro)