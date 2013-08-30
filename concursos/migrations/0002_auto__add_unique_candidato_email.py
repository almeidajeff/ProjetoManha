# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding unique constraint on 'Candidato', fields ['email']
        db.create_unique(u'concursos_candidato', ['email'])


    def backwards(self, orm):
        # Removing unique constraint on 'Candidato', fields ['email']
        db.delete_unique(u'concursos_candidato', ['email'])


    models = {
        u'concursos.candidato': {
            'Meta': {'object_name': 'Candidato'},
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '75'}),
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