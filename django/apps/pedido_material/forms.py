from apps.core.models import Produtos
from .models import PedidoMaterial, PedidoMaterialProduto
from django.forms import ModelForm, modelformset_factory
from django import forms

class PedidoMaterialForm(forms.ModelForm):
    class Meta:
        model = PedidoMaterial
        fields = ('funeraria', 'solicitante')

class PedidoMaterialProdutoForm(forms.ModelForm):
    class Meta:
        model = PedidoMaterialProduto
        fields = ('produto', 'quantidade')


PedidoMaterialFormset = forms.formset_factory(
    form=PedidoMaterialProdutoForm,
    extra=1,
)
