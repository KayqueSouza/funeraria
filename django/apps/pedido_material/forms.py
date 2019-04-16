from apps.core.models import Produtos
from .models import PedidoMaterial
from django.forms import ModelForm, modelformset_factory
from django import forms

PedidoMaterialFormset = modelformset_factory(
    PedidoMaterial,
    fields=('funeraria', 'solicitante', 'quantidade'),
    extra=1,
    widgets={'funeraria': forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Coloque a funeraria aqui'
        })
    }
)