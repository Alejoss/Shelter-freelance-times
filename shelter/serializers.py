from django.contrib.auth.models import User

from rest_framework import serializers

from times.models import Day, Week, Records, ExtraMinutes
from activities.models import TrophySet, Activity


class ExtraMinutesSerializer(serializers.ModelSerializer):
	owner = serializers.Field(source='owner.username')

	class Meta:
		model = ExtraMinutes
		fields =  ('activity', 'operation', 'minutes', 'owner')


class WeekSerializer(serializers.ModelSerializer):

	owner = serializers.Field(source='owner.username')
	date = serializers.CharField(source='get_week_str', read_only=True)

	class Meta:
		model = Week
		fields = ('date', 'hours', 'comments', 'trophy', 'owner')

	def restore_object(self, attrs, instance=None):
		if instance:
			instance.date = attrs.get('date', instance.date)
			instance.comments = attrs.get('comments', instance.comments)
			instance.trophy = attrs.get('trophy', instance.trophy)


class DaySerializer(serializers.ModelSerializer):

	owner = serializers.Field(source='owner.username')
	date = serializers.CharField(source='get_day_str', read_only=True)

	class Meta:
		model = Day
		fields = ('date', 'minutes', 'comments', 'trophy', 'owner')

	def restore_object(self, attrs, instance=None):
		if instance:
			instance.date = attrs.get('date', instance.date)
			instance.comments = attrs.get('comments', instance.comments)
			instance.trophy = attrs.get('trophy', instance.trophy)

			return instance

		return Day(**attrs)


class RecordSerializer(serializers.ModelSerializer):
	activity = serializers.CharField(source='activity.title', read_only=True)
	time_start = serializers.CharField(source='string_time_start', read_only=True)
	time_end = serializers.CharField(source='string_time_end', read_only=True)
	image = serializers.CharField(source='activity.image', read_only=True)

	class Meta:
		model = Records
		fields = ("activity", "time_start", "time_end", "image")


class StartRecordSerializer(serializers.ModelSerializer):
	activity = serializers.PrimaryKeyRelatedField()
	id = serializers.Field()

	class Meta:
		model = Records
		fields = ("activity", "id")


class UserSerializer(serializers.ModelSerializer):

	class Meta:
		model = User
		fields = ('id', 'username')


class TrophySerializer(serializers.ModelSerializer):

	class Meta:
		model = TrophySet


class ActivitySerializer(serializers.ModelSerializer):

	class Meta:
		model = Activity
