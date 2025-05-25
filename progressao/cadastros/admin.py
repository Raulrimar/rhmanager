from django.contrib import admin
from .models import Campo, Atividade, Servidor, Municipio, Situacao, Cedido, Formacao,Classe,MesFerias

# Register your models here.
admin.site.register(Campo)
admin.site.register(Atividade)
admin.site.register(Servidor)
admin.site.register(Municipio)
admin.site.register(Situacao)
admin.site.register(Cedido)
admin.site.register(Formacao)
admin.site.register(Classe)
admin.site.register(MesFerias)

