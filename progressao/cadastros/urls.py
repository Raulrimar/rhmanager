from django.contrib import admin
from django.urls import path, include


from .views import (
    CampoCreate, AtividadeCreate, ServidorCreate,
    CampoUpdateview, AtividadeUpdateview, ServidorDetailView, ServidorUpdateview,
    CampoDelete, AtividadeDelete, ServidorDelete,
    CampoList, AtividadeList, ServidorList
)

urlpatterns = [
    path('', include('paginas.urls')),

    # Cadastrar
    path('cadastrar/campo/', CampoCreate.as_view(), name='cadastrar-campo'),
    path('cadastrar/atividade/', AtividadeCreate.as_view(), name='cadastrar-atividade'),
    path('cadastrar/servidor/', ServidorCreate.as_view(), name='cadastrar-servidor'),

    # Editar
    path('editar/campo/<int:pk>/', CampoUpdateview.as_view(), name='editar-campo'),
    path('editar/atividade/<int:pk>/', AtividadeUpdateview.as_view(), name='editar-atividade'),
    path('editar/servidor/<int:pk>/', ServidorUpdateview.as_view(), name='editar-servidor'),

    # Excluir
    path('excluir/campo/<int:pk>/', CampoDelete.as_view(), name='excluir-campo'),
    path('excluir/atividade/<int:pk>/', AtividadeDelete.as_view(), name='excluir-atividade'),
    path('excluir/servidor/<int:pk>/', ServidorDelete.as_view(), name='excluir-servidor'),

    # Listar
    path('listar/campos/', CampoList.as_view(), name='listar-campos'),
    path('listar/atividades/', AtividadeList.as_view(), name='listar-atividades'),
    path('listar/servidores/', ServidorList.as_view(), name='listar-servidores'),
    path('listar/servidores/<int:pk>/', ServidorDetailView.as_view(), name='detalhar-servidor'),

    # Exibir
    #path('cadastros/servidor/<int:pk>/', ServidorDetailView.as_view(), name='detalhar-servidor'),
]
