from django.urls import path, include
from .views import home, lista_pessoas, lista_veiculos, lista_MovRotativos, lista_mensalistas, lista_MovMensalistas
# importo do core/views.py as views de cada url

#arquivo que controla as urls do meu app /core
urlpatterns = [
    path('', home, name='core_home'),  # quando estiver na url ...core/ eu envio a view home para o usuário
    path('pessoas', lista_pessoas, name='core_lista_pesosoas'),
    path('veiculos', lista_veiculos, name='core_lista_veiculos'),
    path('movrot', lista_MovRotativos, name='core_lista_movrotativos'),
    path('mensalistas', lista_mensalistas, name='core_lista_mensalistas'),
    path('movmens', lista_MovMensalistas, name='core_lista_movmensalistas'),
]
