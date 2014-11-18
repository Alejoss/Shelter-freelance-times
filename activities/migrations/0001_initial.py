# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Activity'
        db.create_table(u'activities_activity', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('owner', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=150, blank=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=500, blank=True)),
            ('image', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
        ))
        db.send_create_signal(u'activities', ['Activity'])

        # Adding model 'TrophySet'
        db.create_table(u'activities_trophyset', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('owner', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=150, blank=True)),
            ('day_0', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('day_1', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('day_2', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('day_3', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('day_4', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('day_5', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('day_6', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('day_7', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('day_8', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('day_9', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('week_0', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('week_1', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('week_2', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('week_3', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('week_4', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('week_5', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('week_6', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('week_7', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('week_8', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('week_9', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
        ))
        db.send_create_signal(u'activities', ['TrophySet'])


    def backwards(self, orm):
        # Deleting model 'Activity'
        db.delete_table(u'activities_activity')

        # Deleting model 'TrophySet'
        db.delete_table(u'activities_trophyset')


    models = {
        u'activities.activity': {
            'Meta': {'object_name': 'Activity'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '150', 'blank': 'True'})
        },
        u'activities.trophyset': {
            'Meta': {'object_name': 'TrophySet'},
            'day_0': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'day_1': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'day_2': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'day_3': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'day_4': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'day_5': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'day_6': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'day_7': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'day_8': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'day_9': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '150', 'blank': 'True'}),
            'week_0': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'week_1': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'week_2': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'week_3': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'week_4': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'week_5': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'week_6': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'week_7': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'week_8': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'week_9': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        },
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['activities']