#from django.shortcuts import render
from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = "paginas/index.html"

class RelatorioView(TemplateView):
    template_name = "paginas/relatorio.html"

class AposentadoView(TemplateView):
    template_name = "paginas/aposentado_form.html"

class ServidorView(TemplateView):
    template_name = "paginas/servidor_form.html"

class CedidoView(TemplateView):
    template_name = "paginas/cedido_form.html"

class FalecidoView(TemplateView):
    template_name = "paginas/falecido_form.html"


