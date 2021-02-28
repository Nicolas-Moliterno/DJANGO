from django.http import HttpResponse
from django.shortcuts import render, render_to_response


def home(request):
    sexo = 'm'
    nome = 'Pedro'
    lista = [
        {'nome':'pedro','sexo':'m'},
          {'nome':'maria','sexo':'f'},
        
    ]
    return render(request,'index.html',{'lista':lista,'sexo' : sexo, 'nome': nome})


