from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView, CreateView, FormView
from django.urls import reverse_lazy

from .models import Circular


class CircularesView(LoginRequiredMixin, ListView):
    context_object_name = "circulares"
    queryset = Circular.objects.all()
    template_name = "circulares/lista_circulares.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Circulares'
        return context


class CircularView(LoginRequiredMixin, ListView):
    context_object_name = "circular"
    queryset = Circular.objects.all()
    template_name = "circulares/circular.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Circular'
        return context


class CircularCreate(LoginRequiredMixin, CreateView):
    model = Circular
    fields = (
        'emitente','setor_destinatario','data_criacao','assunto', 'texto'
    )
    template_name = "circulares/circular_cadastro.html"
    success_url = reverse_lazy('circulares:circulares_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Criar Circular'
        return context

