from apps.core.models import Produtos
from .models import PedidoMaterial
from django.forms import ModelForm
from django.forms.models import inlineformset_factory



class ProdutosForm(ModelForm):
    class Meta:
        model = Produtos
        exclude = ()

ProdutosFormSet = inlineformset_factory(PedidoMaterial, Produtos,
                                            form=ProdutosForm, extra=1)