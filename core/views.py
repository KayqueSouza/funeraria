from django.shortcuts import render, redirect
from .models import Pessoa, Veiculo, MovRotativo, Mensalista, MovMensalista, Alimentacao
from .form import PessoaForm
from django.utils import timezone


def home(request):
    context = {'mensagem':'Ola mundo no contexto'}
    return render(request, 'core/index.html', context)


def lista_pessoas(request):
    pessoas = Pessoa.objects.all()
    form = PessoaForm()
    data = {'pessoas':pessoas, 'form':form}
    return render(request, 'core/lista_pessoas.html', data )


def pessoa_novo(request):
    form = PessoaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_pessoas')


def pessoa_update(request, id):
    data = {}
    pessoa = Pessoa.objects.get(id=id)
    form = PessoaForm(request.POST or None, instance=pessoa)
    data['pessoa']=pessoa
    data['form'] = form
    if request.method == 'GET' or request.method =='POST':
        if form.is_valid():
            form.save()
            print('está no if form.is_valid()')
            return redirect('core_lista_pessoas')
        else:
            print('está no else que depois em return render(request, core/update ...)')
            return render(request, 'core/update_pessoa.html', data)
    
    elif form == None:
        print('eita')

    else:
        print(request.method)
        print('ahhh')

def copa_update(request, id):
    data = {}
    servico = Alimentacao.objects.get(id=2)
    tent = Alimentacao.objetos.filter(id=2).first()
    tent.falecido = tent.falecido + "alterado!"
    tent.save()
    print('passou por aqui')
    dataa = {'servico':servico, 'tent':tent}
    return render(request, 'core/copa.html', dataa )



def pessoa_delete(request, id):
    pessoa = Pessoa.objects.get(id=id)
    if request.method == 'POST' or request.method == 'GET':
        pessoa.delete()
        print('tá no if do pessoa delte')
        return redirect('core_lista_pessoas')
    else:
        print('tá no else do pessoa delte')
        return render(request, 'core/delete_confirm.html', {'pessoa': pessoa})

def lista_veiculos(request):
    veiculos = Veiculo.objects.all()
    return render(request, 'core/lista_veiculos.html', {'veiculos':veiculos})



def lista_movrotativos(request):
    mov_rotativos = MovRotativo.objects.all()
    return render(request, 'core/lista_movrotativos.html', {'mov_rotativos':mov_rotativos})


def lista_mensalista(request):
    mensalistas = Mensalista.objects.all()
    return render(request, 'core/mensalistas.html', {'mensalistas':mensalistas})

def lista_movmensalista(request):
    mov_mensalistas = MovMensalista.objects.all()
    return render(request, 'core/mov-mensalistas.html', {'mov_mensalistas':mov_mensalistas})

def operacional(request):
    alimentacao = Alimentacao.objects.all()
    return render(request, 'core/operacional.html', {'alimentacao':alimentacao})

def copa(request):
    copa = Alimentacao.objects.all()
    data = Alimentacao.objects.get(id=id)
    data.copa = timezone.now()
    data.save()
    return render(request, 'core/copa.html', {'copa': copa, 'data':data})

