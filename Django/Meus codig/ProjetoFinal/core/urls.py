from django.contrib import admin
from django.conf.urls import url
from django.conf import settings
from django.urls import path, include
from django.templatetags.static import static
from django.conf.urls.static import static


from .views import (home,
    lista_pessoas,
    lista_veiculos,
    lista_movrotativos,
    lista_mensalista,
    lista_movmensalista,
    pessoa_novo,
    veiculo_novo,
    movrotativo_novo,
    mensalista_novo,
    movmensalista_novo,
    pessoa_update,
    veiculo_update,
    movrotativo_update,
    mensalista_update,
    movmensalista_update,
    pessoa_delete,
    veiculo_delete,
    movrotativo_delete,
    mensalista_delete,
    movmensalista_delete,
)



urlpatterns = [
    path('',home, name='core_home'),
    path('pessoas/',lista_pessoas, name='core_lista_pessoas'),
    path('pessoa-novo/',pessoa_novo,name='core_pessoas_novo'),
    url(r'^pessoa-update/(?P<id>\d+)/$',pessoa_update,name='core_pessoa_update'),
    url(r'^pessoa-delete/(?P<id>\d+)/$',pessoa_delete,name='core_pessoa_delete'),


    path('veiculos/',lista_veiculos, name='core_lista_veiculos'),
    path('veiculo-novo/',veiculo_novo,name='core_veiculo_novo'),
    url(r'^veiculo-update/(?P<id>\d+)/$',veiculo_update,name='core_veiculo_update'),
    url(r'^veiculo-delete/(?P<id>\d+)/$',veiculo_delete,name='core_veiculo_delete'),

    path('mov-rot/',lista_movrotativos, name='core_lista_movrotativos'),
    path('mov-rot-novo/',movrotativo_novo,name='core_movrotativo_novo'),
    url(r'^movrot-update/(?P<id>\d+)/$',movrotativo_update,name='core_movrotativo_update'),
    url(r'^movrot-delete/(?P<id>\d+)/$',movrotativo_delete,name='core_movrotativo_delete'),

    path('mensalistas/',lista_mensalista, name='core_lista_mensalista'), #name nome da view que é chamada
    path('mensalista-novo/',mensalista_novo,name='core_mensalista_novo'),
    url(r'^mensalista-update/(?P<id>\d+)/$',mensalista_update,name='core_mensalista_update'),
    url(r'^mensalista-delete/(?P<id>\d+)/$',mensalista_delete,name='core_mensalista_delete'),

    path('mov-mensalistas/',lista_movmensalista, name='core_lista_movmensalista'),
    path('mov-mensalista-novo/',movmensalista_novo,name='core_movmensalista_novo'),
    url(r'^mov-mensalista-update/(?P<id>\d+)/$',movmensalista_update,name='core_movmensalista_update'),
    url(r'^mov-mensalista-delete/(?P<id>\d+)/$',movmensalista_delete,name='core_movmensalista_delete'),

    

] 


