from wsgiref.handlers import format_date_time
from django.db import models
from datetime import datetime

# Create your models here.
"""
Nome;
Descrição;
Selo fonográfico;
Ano;
País;
Gênero;
Quantidade.
"""

class disco (models.Model):

    nome = models.CharField(max_length=75, verbose_name='Nome')
    descricao = models.CharField(("Descrição"), max_length=250)
    selo_fonografico = models.CharField(max_length=50)
    ano = models.DateField( auto_now=False, auto_now_add=False)
    pais = models.CharField(('País'),max_length=50)
    genero = models.CharField(("Gênero"), max_length=50)
    quantidade = models.IntegerField()

    
    class Meta:
        verbose_name = ("Disco")
        verbose_name_plural = ("Discos")

    #anoo = ano[:3]
    #mes = ano[7:]
    #dia = ano[4:6]

    

    def __str__ (self):

        self.ano.strftime("%d/%m/%Y")
        return self.nome + ' (' + self.ano.strftime("%d/%m/%Y") +")"
