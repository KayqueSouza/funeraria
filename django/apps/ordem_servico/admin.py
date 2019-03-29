from django.contrib import admin

from .models import (
    Funeraria, LocalRemocao, OrdemServico, Ornamentacao, Preparacao, TaxaPagar, TipoCafe,
    TipoServico,
)


class OrdemServicoAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'falecido', 'funeraria', 'previsao_velorio', 'data_sepultamento')


admin.site.register(TipoServico)
admin.site.register(TaxaPagar)
admin.site.register(LocalRemocao)
admin.site.register(Preparacao)
admin.site.register(OrdemServico, OrdemServicoAdmin)
admin.site.register(Funeraria)
admin.site.register(Ornamentacao)
admin.site.register(TipoCafe)
