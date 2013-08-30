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
    data_hora = DateTimeField(editable=False)
    candidato = ForeignKey(Candidato)
    concurso = models.ForeignKey(Concurso)

    def save(self, *args, **kwargs):
        if not self.id:
            self.data_hora = datetime.today()
        return super(Inscricao, self).save(*args, **kwargs)

    def __unicode__(self):
        return u'%s -- %s' % (self.candidato.nome, self.concurso.titulo)
