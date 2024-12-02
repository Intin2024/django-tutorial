from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('gravadoras', views.list_records, name='lista-gravadoras'),
    path('gravadoras/novo', views.create_records, name='cria-gravadoras'),
    path('gravadoras/editar/<int:id>', views.update_records, name='edita-gravadoras'),
    path('gravadoras/remover/<int:id>', views.remove_records, name='remove-gravadoras'),
    path('novo-usuario', views.create_user, name='cria-usuario'),
    path('musicas/', views.MusicListView.as_view(), name='lista-musicas'),
    path('musicas/novo', views.MusicCreateView.as_view(), name='cria-musicas'),
    path('musicas/editar/<int:pk>', views.MusicUpdateView.as_view(), name='edita-musicas'), # quando se usa class-based views o id precisa ser chamado de pk
    path('musicas/remover/<int:pk>', views.MusicDeleteView.as_view(), name='remove-musicas')
]