from django.db import models
from django.contrib.auth.models import User

class Activity(models.Model):
	owner = models.ForeignKey(User, null=True)
	title = models.CharField(max_length=150, blank=True)
	description = models.CharField(max_length=500, blank=True)
	image = models.URLField(blank=True)

class TrophySet(models.Model):
	owner = models.ForeignKey(User, null=True)
	title = models.CharField(max_length=150, blank=True)
	day_0 = models.URLField(blank=True)
	day_1 = models.URLField(blank=True)
	day_2 = models.URLField(blank=True)
	day_3 = models.URLField(blank=True)
	day_4 = models.URLField(blank=True)
	day_5 = models.URLField(blank=True)
	day_6 = models.URLField(blank=True)
	day_7 = models.URLField(blank=True)
	day_8 = models.URLField(blank=True)
	day_9 = models.URLField(blank=True)
	week_0 = models.URLField(blank=True)
	week_1 = models.URLField(blank=True)
	week_2 = models.URLField(blank=True)
	week_3 = models.URLField(blank=True)
	week_4 = models.URLField(blank=True)
	week_5 = models.URLField(blank=True)
	week_6 = models.URLField(blank=True)
	week_7 = models.URLField(blank=True)
	week_8 = models.URLField(blank=True)
	week_9 = models.URLField(blank=True)
	
