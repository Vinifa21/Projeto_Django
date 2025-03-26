from django.contrib import admin
from .models import Marca, Veiculo, Pessoa,\
    Parametro, MovRotativo, Mensalista, MovMensalista
#importo models para serem usados no admin


class MovRotativoAdmin(admin.ModelAdmin):
    list_display = ("checkin", "checkout", "veiculo", "valor_hora", "pago", "total")


class MovMensalistaAdmin(admin.ModelAdmin):
    list_display = ("mensalista", "data_pgto")



admin.site.register(Marca)
admin.site.register(Veiculo)
admin.site.register(Pessoa)
admin.site.register(Parametro)
admin.site.register(MovRotativo, MovRotativoAdmin)
admin.site.register(Mensalista)
admin.site.register(MovMensalista, MovMensalistaAdmin)
