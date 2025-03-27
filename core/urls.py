from django.urls import path, include
from .views import home
# importo do core/views.py as views de cada url

#arquivo que controla as urls do meu app /core
urlpatterns = [
    path('', home, name='core_home'),  # quando estiver na url ...core/ eu envio a view home para o usuário

]
