from django.shortcuts import render
from django.http import HttpResponse

#view: o que é entregue ao usuário ao ele entrar numa determinada url
#pode ser desde uma string simples com httpResponse, ou um template em html usando render

#para usar templates de um app, criar uma pasta templates dentro dele, aí criar outra pasta
# com o mesmo nome do app, então colocar os templates nessa pasta

def home(request):
    context = {'mensagem': 'Ola, mundo!!!'}
    return render(request, 'core/index.html', context)

def teste(request):
    context = {'mensagem': 'Ola, mundo!!!'} # esse puxa um template direto da pasta raiz
    return render(request, 'base.html', context)  # a pasta que contém os templates da
    # pasta raiz devem ser adicionados aos templates do settings.py

