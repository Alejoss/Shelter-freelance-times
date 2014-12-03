from datetime import datetime

from django.views.generic import ListView, TemplateView
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
#from django.shortcuts import get_object_or_404

from rest_framework import generics, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response

from shelter.permissions import IsOwnerReadOnly
from shelter.serializers import DaySerializer, UserSerializer, WeekSerializer,\
                                StartRecordSerializer, RecordSerializer, \
                                ExtraMinutesSerializer
from times.models import Day, Week, Records, ExtraMinutes
from activities.models import Activity

test_user = User.objects.get(id=1)


class TimeOperationApiView(generics.CreateAPIView):
	model = ExtraMinutes
	serializer_class = ExtraMinutesSerializer

	def pre_save(self, obj):
		obj.owner = self.request.user
		obj.date = datetime.today()


class RecordApiView(generics.RetrieveAPIView):
	queryset = Records.objects.all()
	serializer_class = RecordSerializer


class StartApiView(generics.CreateAPIView):
	model = Records
	serializer_class = StartRecordSerializer

	def pre_save(self, obj):
		obj.owner = self.request.user
		obj.time_start = datetime.today()


class StopApiView(APIView):

	def put(self, request, pk=None, format=None):
		stop_record = Records.objects.latest('id')
		stop_record.time_end = datetime.today()
		stop_record.save()
		return Response(status=status.HTTP_200_OK)


class TodayView(TemplateView):
	template_name = "times/today.html"

	def get_context_data(self, **kwargs):
		actual_time = datetime.today()
		activities = Activity.objects.filter(owner=self.request.user)
		today_records = Records.objects.today()
		if Records.objects.all().count() > 0:
			last_record = Records.objects.latest('id')
		else:
			last_record = None

		context = super(TodayView, self).get_context_data(**kwargs)
		context["today"] = actual_time
		context["activities"] = activities
		context["today_records"] = today_records
		context["last_record"] = last_record

		return context

	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super(TodayView, self).dispatch(*args, **kwargs)


class DayListView(ListView):
	template_name = "times/overview.html"
	model = Day
	context_object_name = "dias"


class WeekListApiView(generics.ListCreateAPIView):

	queryset = Week.objects.all()
	serializer_class = WeekSerializer

	def pre_save(self, obj):
		obj.owner = self.request.user


class DayListApiView(generics.ListCreateAPIView):

	queryset = Day.objects.all()
	serializer_class = DaySerializer
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

	def pre_save(self, obj):
		obj.owner = self.request.user


class DayApiView(generics.RetrieveUpdateDestroyAPIView):

	queryset = Day.objects.all()
	serializer_class = DaySerializer
	permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerReadOnly)

	def pre_save(self, obj):
		obj.owner = self.request.user


class UserApiListView(generics.ListAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer


class UserApiDetailView(generics.RetrieveAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer
