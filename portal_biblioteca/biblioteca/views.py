from django.http import HttpResponse
from django.template import loader
from .models import Livro, TCC
from django.contrib.auth.decorators import login_required

def principal(request):
    template = loader.get_template('principal.html')
    return HttpResponse(template.render())

def livros(request):         # atualize esta função
    livros = Livro.objects.all().values()
    template = loader.get_template('livros.html')
    context = {
        'livros': livros,
    }
    return HttpResponse(template.render(context, request))

def tccs(request):         # atualize esta função
    tccs = TCC.objects.all().values()
    template = loader.get_template('tccs.html')
    context = {
        'tccs': tccs,
    }
    return HttpResponse(template.render(context, request))

def tcc_detalhes(request, id):
    tcc = TCC.objects.get(id=id)
    template = loader.get_template('tcc_detalhes.html')
    context = {
        'tcc': tcc,
    }
    return HttpResponse(template.render(context, request))

@login_required(login_url="/auth/login")
def dashboard(request):
    template = loader.get_template('dashboard.html')
    # Você pode acessar o usuário logado através de request.user
    user = request.user
    # Agora você pode fazer qualquer coisa com o objeto 'user', como acessar seus campos, por exemplo:
    username = user.username
    email = user.email
    context = {
        'usuario': username,
        'email': email,
    }
    return HttpResponse(template.render(context, request))