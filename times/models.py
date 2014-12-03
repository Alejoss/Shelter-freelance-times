import datetime
import pytz

from django.db import models
from django.contrib.auth.models import User

from activities.models import Activity


class Day(models.Model):
	owner = models.ForeignKey(User, null=True)
	date = models.DateTimeField(null=True)
	minutes = models.IntegerField(default=0, null=True)
	comments = models.CharField(blank=True, max_length=500)
	trophy = models.CharField(blank=True, max_length=250)

	def get_day_str(self):
		return self.date.strftime("%A %d. %B")


class Week(models.Model):
	owner = models.ForeignKey(User, null=True)
	date = models.DateTimeField(null=True)
	hours = models.IntegerField(default=0, null=True)
	comments = models.CharField(blank=True, max_length=500)
	trophy = models.CharField(blank=True, max_length=250)

	def get_week_str(self):
		week_number = self.date.isocalendar()[1]
		month = self.date.strftime("%b")
		return "%s %s" % (week_number, month)


class RecordManager(models.Manager):

	use_for_related_fields = True

	def today(self, **kwargs):
		today = datetime.datetime.now(pytz.utc)
		reference_date = datetime.datetime(today.year, today.month, today.day, tzinfo=pytz.utc)

		return self.filter(time_start__gte=reference_date, **kwargs)


class Records(models.Model):
	owner = models.ForeignKey(User, null=True)
	activity = models.ForeignKey(Activity, null=True)
	time_start = models.DateTimeField(null=True)
	time_end = models.DateTimeField(null=True)
	objects = RecordManager()

	def is_running(self):
		if self.time_end is None:
			return True
		else:
			return False

	def total_time(self):
		return ((self.time_end-self.time_start).seconds)/60

	def string_time_start(self):
		if self.time_start:
			return self.time_start.strftime("%H:%M %P")
		else:
			return None

	def string_time_end(self):
		if self.time_end:
			return self.time_end.strftime("%H:%M %P")
		else:
			return None

	def __unicode__(self):
		return "%s - %s" % (self.activity.title, self.string_time_start())


class ExtraMinutes(models.Model):

	operation_choices = (("PLUS", "plus"), ("MINUS", "minus"),)

	owner = models.ForeignKey(User, null=True)
	activity = models.ForeignKey(Activity, null=True)
	minutes = models.IntegerField(default=0)
	operation = models.CharField(max_length=10, choices=operation_choices)
	date = models.DateTimeField(null=True)
