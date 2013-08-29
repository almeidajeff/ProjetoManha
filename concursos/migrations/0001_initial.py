# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Concurso'
        db.create_table(u'concursos_concurso', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('titulo', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('data', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal(u'concursos', ['Concurso'])

        # Adding model 'Candidato'
        db.create_table(u'concursos_candidato', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
        ))
        db.send_create_signal(u'concursos', ['Candidato'])

        # Adding model 'Inscricao'
        db.create_table(u'concursos_inscricao', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('data_hora', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('candidato', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['concursos.Candidato'])),
            ('concurso', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['concursos.Concurso'])),
        ))
        db.send_create_signal(u'concursos', ['Inscricao'])

        # Adding unique constraint on 'Inscricao', fields ['candidato', 'concurso']
        db.create_unique(u'concursos_inscricao', ['candidato_id', 'concurso_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'Inscricao', fields ['candidato', 'concurso']
        db.delete_unique(u'concursos_inscricao', ['candidato_id', 'concurso_id'])

        # Deleting model 'Concurso'
        db.delete_table(u'concursos_concurso')

        # Deleting model 'Candidato'
        db.delete_table(u'concursos_candidato')

        # Deleting model 'Inscricao'
        db.delete_table(u'concursos_inscricao')


    models = {
        u'concursos.candidato': {
            'Meta': {'object_name': 'Candidato'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'concursos.concurso': {
            'Meta': {'object_name': 'Concurso'},
            'data': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'concursos.inscricao': {
            'Meta': {'unique_together': "(('candidato', 'concurso'),)", 'object_name': 'Inscricao'},
            'candidato': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['concursos.Candidato']"}),
            'concurso': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['concursos.Concurso']"}),
            'data_hora': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['concursos']