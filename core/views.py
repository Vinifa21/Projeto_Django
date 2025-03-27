from django.shortcuts import render
from django.http import HttpResponse
from .models import Pessoa, Veiculo, MovRotativo, Mensalista, MovMensalista  #importo dados de um model especifico e posso injetalo em um template

#view: o que é entregue ao usuário ao ele entrar numa determinada url
#pode ser desde uma string simples com httpResponse, ou um template em html usando render

#para usar templates de um app, criar uma pasta templates dentro dele, aí criar outra pasta
# com o mesmo nome do app, então colocar os templates nessa pasta

def home(request):
    context = {'mensagem': 'Ola, mundo!!!'} # variavel que sera injetada no template
    return render(request, 'core/index.html', context)  #tenho q add o index.html
    # na pasta templates/core desse app

def lista_pessoas(request):
    pessoas = Pessoa.objects.all  #injeto a variavel pessoas (contem todos os objetos de pessoas) no template
    return render(request, 'core/lista_pessoas.html', {'pessoas': pessoas}) # passo para dentro do template com o nome 'pessoas', a variavel pessoa


def lista_veiculos(request):
    todos_veiculos = Veiculo.objects.all
    return render(request, 'core/lista_veiculos.html', {'todos_veiculos': todos_veiculos})

def lista_MovRotativos(request):
    MovsRotativos = MovRotativo.objects.all
    return render(request, 'core/lista_MovsRotativos.html', {'variavel_injetada': MovsRotativos})


def lista_mensalistas(request):
    mensalistas = Mensalista.objects.all
    return render(request, 'core/lista_mensalista.html', {'mensalistas': mensalistas})


def lista_MovMensalistas(request):
    movsmensalistas = MovMensalista.objects.all
    return render(request, 'core/lista_movsmensalistas.html', {'movs': movsmensalistas})



def teste(request):
    context = {'mensagem': 'Ola, mundo!!!'} # esse puxa um template direto da pasta raiz
    return render(request, 'base.html', context)  # a pasta que contém os templates da
    # pasta raiz devem ser adicionados aos templates do settings.py

