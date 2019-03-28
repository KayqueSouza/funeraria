from django.contrib import admin
from .models import (Marca, Veiculo, Pessoa, Parametros, 
MovRotativo, Mensalista, MovMensalista, Especies, Abrangencia,
 TipoServico, TaxasPagar, LocalRemocao, Preparacao,
  Alimentacao, Funerarias, Ornamentacao, Cafe)

class MovRotativoAdmin(admin.ModelAdmin):
    list_display=('checkin', 'checkout', 'valor_hora', 'pago', 'total','horas_total','veiculo')
    def veiculo(self,obj):
        return obj.veiculo


class MovMensalistaAdmin(admin.ModelAdmin):
    list_display=('mensalista','dt_pgto','dt_pgto')


class AlimentacaoAdmin(admin.ModelAdmin):
    list_display=('os','falecido', 'funeraria','prev_vel','data_sep')

admin.site.register(Marca)
admin.site.register(Veiculo)
admin.site.register(Pessoa)
admin.site.register(Parametros)
admin.site.register(MovMensalista, MovMensalistaAdmin)

admin.site.register(Mensalista)
admin.site.register(MovRotativo, MovRotativoAdmin)
admin.site.register(Especies)
admin.site.register(Abrangencia)
admin.site.register(TipoServico)  
admin.site.register(TaxasPagar)
admin.site.register(LocalRemocao)
admin.site.register(Preparacao)
admin.site.register(Alimentacao, AlimentacaoAdmin)
admin.site.register(Funerarias)
admin.site.register(Ornamentacao)
admin.site.register(Cafe)