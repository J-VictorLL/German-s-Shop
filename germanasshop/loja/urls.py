from django.urls import path
from . import views

app_name = 'loja'
urlpatterns = [
    path('', views.index, name='inicio'),
    path('forum/', views.forum, name='forum'),
    path('cesta/', views.cesta, name='cesta'),
    path('produto/<int:id_produto>/', views.produto, name='produto'),
    path('historico/', views.historico, name='historico'),
]