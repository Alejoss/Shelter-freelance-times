# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Day'
        db.create_table(u'times_day', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateTimeField')(null=True)),
            ('minutes', self.gf('django.db.models.fields.IntegerField')(default=0, null=True)),
            ('comments', self.gf('django.db.models.fields.CharField')(max_length=500, null=True, blank=True)),
            ('trofee', self.gf('django.db.models.fields.IntegerField')(default=0, null=True)),
        ))
        db.send_create_signal(u'times', ['Day'])


    def backwards(self, orm):
        # Deleting model 'Day'
        db.delete_table(u'times_day')


    models = {
        u'times.day': {
            'Meta': {'object_name': 'Day'},
            'comments': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'minutes': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True'}),
            'trofee': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True'})
        }
    }

    complete_apps = ['times']