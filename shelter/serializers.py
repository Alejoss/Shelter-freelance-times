from django.contrib.auth.models import User

from rest_framework import serializers

from times.models import Day, Week
from activities.models import TrophySet, Activity


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
