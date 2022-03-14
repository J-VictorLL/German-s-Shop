from django.urls import path
from . import views

app_name = 'loja'
urlpatterns = [
    path('', views.index, name='loja'),
    path('login/',views.login,name='login')
]