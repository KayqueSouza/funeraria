from django.contrib import admin

from .models import (
  PedidoMaterial,
  Produtos,
)


class PedidoMaterialAdmin(admin.ModelAdmin):
  list_display = ('funeraria','solicitante','produto','quantidade','status_atual')



admin.site.register(PedidoMaterial, PedidoMaterialAdmin)
