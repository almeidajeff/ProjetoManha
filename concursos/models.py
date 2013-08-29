# -*- coding: utf-8 -*-
from django.db import models
from django.db.models import CharField, EmailField, DateTimeField, ForeignKey ,\
    DateField
from datetime import datetime

# Create your models here.

class Concurso(models.Model):
    """ Dados do concurso """
    titulo = CharField(max_length=200)
    data = DateField()
    
    def __unicode__(self):
        return self.titulo

class Candidato(models.Model):
    """Dados do candidato que pode inscrever-se em um concurso."""
    nome = CharField(max_length=100)
    email = EmailField(unique=True)
    
    def __unicode__(self):
        return self.nome

class Inscricao(models.Model):
    """Inscrições de candidatos em concursos."""
    #data_hora = DateTimeField(default=datetime.now(), blank=True)
    data_hora = DateTimeField('data inscricao', blank=True, null=True)
    candidato = ForeignKey(Candidato)
    concurso = models.ForeignKey(Concurso)

    def __unicode__(self):
        return u'%s -- %s' % (self.candidato.nome, self.concurso.titulo)
    
    class Meta:
        # O mesmo candidato não pode inscrever-se duas vezes em um mesmo concurso
        # https://docs.djangoproject.com/en/dev/ref/models/options/#unique-together
        unique_together = ('candidato', 'concurso') 