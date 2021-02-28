from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from .models import (Pessoa,
             Veiculo,
             MovRotativo,
             Mensalista,
             MovMensalista,

)

from .forms import (
        PessoasForm,
        VeiculoForm,
        MovRotativoForm,
        MensalistaForm,
        MovMensalistaForm,
)   



# Create your views here.

@login_required
def home(request):
    context = {'mensagem': 'Ola mundo...'}
    return render(request,'core/index.html',context)



@login_required
def lista_pessoas(request):
    pessoas = Pessoa.objects.all()
    form = PessoasForm()
    data = {'pessoas' : pessoas, 'form' : form}
    return render(request,'core/lista_pessoas.html',data)


@login_required
def pessoa_novo(request):
    form = PessoasForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_pessoas') #redirect redireciona para a url que eu quero que ela redirecione


@login_required
def pessoa_update(request,id):
    data = {}
    pessoa = Pessoa.objects.get(id=id)
    form = PessoasForm(request.POST or None,instance=pessoa)
    data['pessoa'] = pessoa
    data['form'] = form
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_pessoas')
    else:
        return render(request,'core/update_pessoa.html',data)


@login_required
def pessoa_delete(request,id):
    pessoa = Pessoa.objects.get(id=id)
    if request.method == 'POST':
        pessoa.delete()
        return redirect('core_lista_pessoas')
    else:
        return render(request,'core/delete_confirm.html',{'obj' : pessoa})



@login_required
def lista_veiculos(request):
    form = VeiculoForm()
    veiculos = Veiculo.objects.all()
    data = {'veiculos' : veiculos, 'form':form}
    return render(request,'core/lista_veiculos.html',data)
                                                        #variavel que passa para o html


@login_required
def veiculo_novo(request):
    form = VeiculoForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_veiculos')


@login_required
def veiculo_update(request,id):
    data = {}
    veiculo = Veiculo.objects.get(id=id)
    form = VeiculoForm(request.POST or None,instance=veiculo)
    data['veiculo'] = veiculo
    data['form'] = form
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_veiculos')
    else:
        return render(request,'core/update_veiculo.html',data)


@login_required
def veiculo_delete(request,id):
    veiculo = Veiculo.objects.get(id=id)
    if request.method == 'POST':
        veiculo.delete()
        return redirect('core_lista_veiculos')
    else:
        return render(request,'core/delete_confirm.html',{'obj' : veiculo})


@login_required
def lista_movrotativos(request):
    form = MovRotativoForm()
    mov_rot = MovRotativo.objects.all()
    data = {'mov_rot' : mov_rot, 'form' : form}
    return render(request,'core/lista_movrotativos.html', data)
                                                        #variavel que passa para o html


@login_required
def movrotativo_novo(request):
    form = MovRotativoForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_movrotativos')


@login_required
def movrotativo_update(request,id):
    data = {}
    movrotativo = MovRotativo.objects.get(id=id)
    form = MovRotativoForm(request.POST or None,instance=movrotativo)
    data['movrotativo'] = movrotativo
    data['form'] = form
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_movrotativos')
    else:
        return render(request,'core/update_movrotativo.html',data)


@login_required
def  movrotativo_delete(request,id):
    movrotativo = MovRotativo.objects.get(id=id)
    if request.method == 'POST':
        movrotativo.delete()
        return redirect('core_lista_movrotativos')
    else:
        return render(request,'core/delete_confirm.html',{'obj' : movrotativo})



@login_required
def lista_mensalista(request):
    form = MensalistaForm()
    mensalistas = Mensalista.objects.all()
    data = {'mensalistas' : mensalistas, 'form' : form}
    return render(request,'core/lista_mensalistas.html', data)
                                                        #variavel que passa para o html


@login_required
def mensalista_novo(request):
    form = MensalistaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_mensalista')


@login_required
def mensalista_update(request,id):
    data = {}
    mensalista = Mensalista.objects.get(id=id)
    form = MensalistaForm(request.POST or None,instance=mensalista)
    data['mensalista'] = mensalista
    data['form'] = form
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_mensalista')
    else:
        return render(request,'core/update_mensalista.html',data)


@login_required
def mensalista_delete(request,id):
    mensalista = Mensalista.objects.get(id=id)
    if request.method == 'POST':
        mensalista.delete()
        return redirect('core_lista_mensalista')
    else:
        return render(request,'core/delete_confirm.html',{'obj' : mensalista})


@login_required
def lista_movmensalista(request):
    form = MovMensalistaForm()
    mov_mensalistas = MovMensalista.objects.all()
    data = {'mov_mensalistas' : mov_mensalistas,'form':form}
    return render(request,'core/lista_movmensalistas.html',data)
                                                        #variavel que passa para o html


@login_required
def movmensalista_novo(request):
    form = MovMensalistaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_movmensalista')


@login_required
def movmensalista_update(request,id):
    data = {}
    mov_mensalista = MovMensalista.objects.get(id=id)
    form = MovMensalistaForm(request.POST or None,instance=mov_mensalista)
    data['mov_mensalista'] = mov_mensalista
    data['form'] = form
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_movmensalista')
    else:
        return render(request,'core/update_movmensalista.html',data)



@login_required
def movmensalista_delete(request,id):
    movmensalista = MovMensalista.objects.get(id=id)
    if request.method == 'POST':
        movmensalista.delete()
        return redirect('core_lista_movmensalista')
    else:
        return render(request,'core/delete_confirm.html',{'obj' : movmensalista})