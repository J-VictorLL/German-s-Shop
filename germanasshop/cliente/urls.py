from django.urls import path
from django.contrib.auth import views as auth_view
from . import views

app_name = 'cliente'
urlpatterns = [
    # ex: /polls/
    # path('', views.index, name='index'),
    # ex: /polls/5/
    #path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    # path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    #path('<int:question_id>/vote/', views.vote, name='vote'),
    # ex: /polls/
    path("cadastro/", views.cadastro, name='cadastro'),

    path('login/', views.login, name='login'),
    path('logindjango/',  auth_view.LoginView.as_view(template_name= 'cadastro/login.html') , name='logindjango')
    
]
