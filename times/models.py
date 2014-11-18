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


class Records(models.Model):
	owner = models.ForeignKey(User, null=True)
	activity = models.ForeignKey(Activity, null=True)
	time_start = models.DateTimeField(null=True)
	time_end = models.DateTimeField(null=True)

	def is_running(self):
		if self.time_end is None:
			return True
		else:
			return False

