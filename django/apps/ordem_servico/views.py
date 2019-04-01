from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView, CreateView, FormView

from .models import OrdemServico
#from .forms import OrdemServicoForm


class OrdemServicoView(LoginRequiredMixin, ListView):
    context_object_name = "ordem_servicos"
    queryset = OrdemServico.objects.all()
    template_name = "ordem_servico/listagem.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Ordem de Serviço'
        return context

class CopaView(LoginRequiredMixin, ListView):
    context_object_name = "ordem_servicos"
    queryset = OrdemServico.objects.all()
    template_name = "ordem_servico/listagem_copa.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Copa'
        return context




class OrdemServicoCreate(LoginRequiredMixin, CreateView):
    model = OrdemServico
    fields = '__all__'
    template_name = "ordem_servico/os_cadastro.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Criar Ordem de Serviço'
        return context

class AgentesView(LoginRequiredMixin, ListView):
    context_object_name = "ordem_servicos"
    queryset = OrdemServico.objects.all()
    template_name = "ordem_servico/agentes.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Agentes'
        return context


def copa(request):
    servico = OrdemServico.objects.all()
    return render(request, 'ordem_servico/copa.html', {'servico': servico})


def copa_update(request, id):
    servico = OrdemServico.objects.get(id=2)
    tent = OrdemServico.objetos.filter(id=2).first()
    tent.falecido = tent.falecido + "alterado!"
    tent.save()
    print('passou por aqui')
    data = {'servico': servico, 'tent': tent}
    return render(request, 'ordem_servico//copa.html', data)
