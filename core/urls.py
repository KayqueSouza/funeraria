from django.urls import path, include
from .views import (home, lista_pessoas, lista_veiculos, lista_movrotativos,
 lista_mensalista, lista_movmensalista, pessoa_novo,pessoa_update,
  pessoa_delete, operacional, copa)

urlpatterns = [
    path('pessoas/',lista_pessoas, name='core_lista_pessoas'),
    path('pessoas-novo/',pessoa_novo, name='core_pessoa_novo'),
    path('pessoa-update/<int:id>/',pessoa_update, name='core_pessoa_update'),
    path('pessoa-delete/<int:id>/',pessoa_delete, name='core_pessoa_delete'),
    path('veiculos/',lista_veiculos, name='core_lista_veiculos'),
    path('mov-rot-list/', lista_movrotativos, name='core_lista_movrotativos'),
    path('mensalistas/', lista_mensalista, name='core_lista_mensalista'),
    path('mov-mensal/', lista_movmensalista, name='core_lista_movmensalista'),
    path('operacional/', operacional, name = 'operacional'),
    path('copa/', copa, name='copa_copa'),
    path('', home, name='core_home')


]