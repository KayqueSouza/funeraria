from django.shortcuts import render, redirect
from .models import Servico
from django.utils import timezone


def home(request):
    context = {'mensagem':'Ola mundo no contexto'}
    return render(request, 'core/index.html', context)




def copa_update(request, id):
    data = {}
    servico = Servico.objects.get(id=2)
    tent = Servico.objetos.filter(id=2).first()
    tent.falecido = tent.falecido + "alterado!"
    tent.save()
    print('passou por aqui')
    dataa = {'servico':servico, 'tent':tent}
    return render(request, 'core/copa.html', dataa)





def operacional(request):
    servico = Servico.objects.all()
    return render(request, 'core/operacional.html', {'servico':servico})

def copa(request):
    copa = Servico.objects.all()

    return render(request, 'core/copa.html', {'copa': copa})

