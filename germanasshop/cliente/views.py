
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     context = {'latest_question_list': latest_question_list}
#     return render(request, 'cadastro/index.html', context)


# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'cadastro/detail.html', {'question': question})


# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'cadastro/results.html', {'question': question})


# def vote(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     try:
#         selected_choice = question.choice_set.get(pk=request.POST['choice'])
#     except (KeyError, Choice.DoesNotExist):
#         # Redisplay the question voting form.
#         return render(request, 'cadastro/detail.html', {
#             'question': question,
#             'error_message': "You didn't select a choice.",
#         })
#     else:
#         selected_choice.votes += 1
#         selected_choice.save()
#         return HttpResponseRedirect(reverse('cadastro:results', args=(question.id,)))


def cadastro(request):
    #return render(request,'cadastro/cadastro.html')
    #cadastro = get_object_or_404(Cadastro)
    try:
        nome = request.POST['nome']
        cpf = request.POST['cpf']
        email = request.POST['email']
        senha = request.POST['senha']
        confirmar = request.POST['confirmar']
    except (KeyError):
        return render(request, 'cadastro/cadastro.html')
    else:
        if(nome != '' and cpf  != '' and email != ''):
            if(senha == confirmar):
              
                #create_user(username, email=None, password=None, **extra_fields)
                user = User.objects.create_user(nome, email=email, password=senha)
                user.save()
                #UserManager.create_user(nome, email=email, password=senha)
                c.save()
                print(nome, email, senha)
        return render(request, 'cadastro/login.html')
    
def login(request):
    try:
        nome = request.POST['nome']
        senha = request.POST['senha']
    except (KeyError):
        return render(request, 'cadastro/login.html')
    else:
        user = authenticate(username=nome, password=senha)
        if user:
            request.session['id_usuario'] = user.id
            return render(request, 'cadastro/carregando.html')
        return render(request, 'cadastro/erro.html')
        
        
        
