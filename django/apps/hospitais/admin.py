from django.contrib import admin

from .models import ( ObitosHospitais)


class ObitosHospitaisAdmin(admin.ModelAdmin):
    pass


admin.site.register(ObitosHospitais)
