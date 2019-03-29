from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import TemplateView

from .models import Servico


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = "core/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Dashboard'
        context['mensagem'] = 'Ola mundo no contexto'
        return context


def copa_update(request, id):
    servico = Servico.objects.get(id=2)
    tent = Servico.objetos.filter(id=2).first()
    tent.falecido = tent.falecido + "alterado!"
    tent.save()
    print('passou por aqui')
    data = {'servico': servico, 'tent': tent}
    return render(request, 'core/copa.html', data)


def operacional(request):
    ordem_servicos = Servico.objects.all()
    return render(request, 'core/operacional.html', {'ordem_servicos': ordem_servicos})


def copa(request):
    servico = Servico.objects.all()

    return render(request, 'core/copa.html', {'servico': servico})
