from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView, UpdateView, DeleteView, ListView, DetailView
)
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin

from .models import (
    Campo, Atividade, Classe, Servidor,
    Cedido, Municipio, Situacao
)
from .forms import ServidorForm

from django.db.models import Count
from .models import Servidor

########## CREATE VIEW ##########

class CampoCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = u"administrador"
    model = Campo
    fields = ['nome', 'descricao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')

class AtividadeCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Atividade
    fields = ['numero', 'descricao', 'pontos', 'detalhes', 'campo']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')

class ServidorCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = u"administrador"
    model = Servidor
    fields = ['foto','nome','cargo', 'data_admissao','lotacao','ultima_lotacao','formacao','matricula','telefone','proxima_promocao','email','situacao','cedido','municipio','observacao','documentacao','classe','sexo','mesFerias','inicioferias','terminoferias','cancelamentos','origem']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-servidores')

class CedidoCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Cedido
    fields = ['nome']
    template_name = 'cadastrar/form.html'
    success_url = reverse_lazy('index')

class SituacaoCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Situacao
    fields = ['nome']
    template_name = 'cadastro/form.html'
    success_url = reverse_lazy('index')

class MunicipioCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Municipio
    fields = ['nome']
    template_name = 'cadastrar/form.html'
    success_url = reverse_lazy('index')

class ClasseCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Classe
    fields = ['nome']
    template_name = 'cadastrar/form.html'
    success_url = reverse_lazy('index')


########## UPDATE VIEW ##########

class CampoUpdateview(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    group_required = u"administrador"
    model = Campo
    fields = ['nome', 'descricao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')

class AtividadeUpdateview(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Atividade
    fields = ['numero', 'descricao', 'pontos', 'detalhes', 'campo']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')

class ServidorUpdateview(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    group_required = u"administrador"
    model = Servidor
    fields = ['foto','nome','cargo', 'data_admissao','lotacao','ultima_lotacao','formacao','matricula','telefone','proxima_promocao','email','situacao','cedido','municipio','observacao','documentacao','classe','sexo','mesFerias','inicioferias','terminoferias','cancelamentos','origem']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-servidores')


########## DELETE VIEW ##########

class CampoDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = u"administrador"
    model = Campo
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('index')

class AtividadeDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Atividade
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('index')

class ServidorDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = u"administrador"
    model = Servidor
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-servidores')


########## LIST VIEW ##########

class CampoList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Campo
    template_name = 'cadastros/listas/campo.html'

class AtividadeList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Atividade
    template_name = 'cadastros/listas/atividade.html'

from django.db.models import Q

class ServidorList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    group_required = u"administrador"
    model = Servidor
    template_name = 'cadastros/listas/servidor.html'
    context_object_name = 'object_list'
    paginate_by = 50

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get("q")
        if query:
            queryset = queryset.filter(
                Q(nome__icontains=query) |
                Q(matricula__icontains=query) |
                Q(cargo__icontains=query) |
                Q(lotacao__icontains=query)
            )
        return queryset


########## DETAIL VIEW ##########

class ServidorDetailView(GroupRequiredMixin, LoginRequiredMixin, DetailView):
    login_url = reverse_lazy('login')
    group_required = u"administrador"
    model = Servidor
    template_name = 'cadastros/listas/servidor_detalhe.html'
    context_object_name = 'servidor'


########## VIEW PERSONALIZADA ##########

def criar_servidor(request):
    if request.method == 'POST':
        form = ServidorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listar-servidores')  # Corrigido
    else:
        form = ServidorForm()
    return render(
        request, 'cadastros/form.html', {'form': form}
        )


