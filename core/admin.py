from django.contrib import admin
from .models import (Especies, Abrangencia,
 TipoServico, TaxasPagar, LocalRemocao, Preparacao,
  Servico, Funerarias, Ornamentacao, Cafe)



class ServicoAdmin(admin.ModelAdmin):
    list_display=('os','falecido', 'funeraria','prev_vel','data_sep')


admin.site.register(Especies)
admin.site.register(Abrangencia)
admin.site.register(TipoServico)  
admin.site.register(TaxasPagar)
admin.site.register(LocalRemocao)
admin.site.register(Preparacao)
admin.site.register(Servico, ServicoAdmin)
admin.site.register(Funerarias)
admin.site.register(Ornamentacao)
admin.site.register(Cafe)