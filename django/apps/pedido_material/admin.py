from django.contrib import admin

from .models import (
  PedidoMaterial,
  Produtos,
)


class PedidoMaterialAdmin(admin.ModelAdmin):
  list_display = ('funeraria','solicitante','status_atual')



admin.site.register(PedidoMaterial, PedidoMaterialAdmin)
