from django.shortcuts import render, redirect
from core.models import Evento
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# redireciona p/ uma url existente
#def index(request):
    #return redirect('/agenda/')

def login_user(request):
    return render(request,'login.html')

def submit_login(request):
    # Se a requisição for do tipo POST
    if request.POST:
        username = request.POST.get('usuario')
        password = request.POST.get('senha')
        usuario = authenticate(username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('/')
        else:
            messages.error(request, "Usuário ou senha inválida !")

    return redirect('/')

def logout_user(request):
    logout(request)
    return redirect('/')

# decorator
@login_required(login_url='/login/')
def lista_eventos(request):
    usuario = request.user
    evento = Evento.objects.filter(usuario=usuario)
    dados = { 'eventos':evento }
    return render(request, 'agenda.html', dados)

@login_required(login_url='/login/')
def evento(request):
    return render(request, 'evento.html')

@login_required(login_url='/login/')
def submit_evento(request):
    if request.POST:
        titulo = request.POST.get('titulo')
        data_evento = request.POST.get('data_evento')
        descricao = request.POST.get('descricao')
        usuario = request.user
        Evento.objects.create(titulo=titulo,
                              data_event=data_evento,
                              descricao=descricao,
                              usuario=usuario)
    return redirect('/')

