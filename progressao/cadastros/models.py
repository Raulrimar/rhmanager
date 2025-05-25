# models.py

from django.db import models

class Campo(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.CharField(max_length=150, verbose_name='Descrição')

    def __str__(self):
        return "{} ({})".format(self.nome, self.descricao)

class Atividade(models.Model):
    numero = models.IntegerField(verbose_name="Número")
    descricao = models.CharField(max_length=150, verbose_name="Descrição")
    pontos = models.DecimalField(decimal_places=2, max_digits=4)
    detalhes = models.CharField(max_length=100)
    campo = models.ForeignKey(Campo, on_delete=models.PROTECT)

    def __str__(self):
        return "{} - {} ({})".format(self.numero, self.descricao, self.campo.nome)

class Municipio(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return "{}".format(self.nome)

class Situacao(models.Model):
    nome = models.CharField(max_length=50, verbose_name="Situação")

    def __str__(self):
        return "{}".format(self.nome)

class Cedido(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return "{}".format(self.nome)

class Formacao(models.Model):
    nome = models.CharField(max_length=50, verbose_name="Formação")

    def __str__(self):
        return "{}".format(self.nome)

class Classe(models.Model):
    nome = models.CharField(max_length=5)

    def __str__(self):
        return "{}".format(self.nome)
    
class MesFerias(models.Model):
    nome = models.CharField(max_length=50, verbose_name="Mês Férias")
    def __str__(self):
        return "{}".format(self.nome)

class Servidor(models.Model):
    SEXO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('O', 'Outro'),
    ]


    documentacao = models.FileField(upload_to='pdf/', verbose_name="Documentação", blank=True, null=True)
    foto = models.ImageField(upload_to='fotos/', null=True, blank=True)
    nome = models.CharField(max_length=255, blank=True, null=True)
    cargo = models.CharField(max_length=100, blank=True, null=True)
    data_admissao = models.DateField(verbose_name="Data de Admissão", blank=True, null=True)
    lotacao = models.CharField(verbose_name="Lotação", max_length=100, blank=True, null=True)
    ultima_lotacao = models.CharField(max_length=100, verbose_name="Ultima Lotação", blank=True, null=True)
    matricula = models.CharField(verbose_name="Matrícula", max_length=100, unique=True)
    telefone = models.CharField(max_length=100, blank=True, null=True)
    proxima_promocao = models.CharField(verbose_name="Próxima Promoção", max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    observacao = models.CharField(verbose_name="Observação", max_length=999, blank=True, null=True)
    inicioferias = models.DateField(blank=True, null=True, verbose_name="Início Férias")
    terminoferias = models.DateField(blank=True, null=True, verbose_name="Termino Férias")
    origem = models.TextField(max_length=1000, blank=True, null=True, verbose_name="Origens")
    cancelamentos = models.TextField(max_length=1000, blank=True, null=True, verbose_name="Alterações/Cancelamentos")
    

    municipio = models.ForeignKey(Municipio, on_delete=models.PROTECT, verbose_name="Município", blank=True, null=True)
    situacao = models.ForeignKey(Situacao, on_delete=models.PROTECT, verbose_name="Situação", blank=True, null=True)
    cedido = models.ForeignKey(Cedido, on_delete=models.PROTECT)
    formacao = models.ForeignKey(Formacao, on_delete=models.PROTECT, verbose_name="Formação", blank=True, null=True)
    classe = models.ForeignKey(Classe, on_delete=models.PROTECT, null=True, blank=True)
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES, blank=True, null=True, verbose_name='Sexo')
    mesFerias = models.ForeignKey(MesFerias, on_delete=models.PROTECT, blank=True, null=True, verbose_name="Mês de Férias")


    def __str__(self):
        return "{}".format(self.nome)
