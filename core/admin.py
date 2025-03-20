from django.contrib import admin
from .models import Marca, Veiculo, Pessoa
#importo models para serem usados no admin

admin.site.register(Marca)
admin.site.register(Veiculo)
admin.site.register(Pessoa)
