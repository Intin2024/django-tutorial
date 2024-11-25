from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('gravadoras', views.list_records, name='lista-gravadoras'),
    path('gravadoras/novo', views.create_records, name='cria-gravadoras'),
    path('gravadoras/editar/<int:id>', views.update_records, name='edita-gravadoras'),
    path('gravadoras/remover/<int:id>', views.remove_records, name='remove-gravadoras')
]