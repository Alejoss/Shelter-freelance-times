import datetime

from django.views.generic import ListView, TemplateView
from django.contrib.auth.models import User

from rest_framework import generics, permissions

from shelter.permissions import IsOwnerReadOnly
from shelter.serializers import DaySerializer, UserSerializer, WeekSerializer
from times.models import Day, Week, Records


class TodayView(TemplateView):
	template_name = "times/today.html"
	if Records.objects.all().count() > 0:
		last_record = Records.objects.latest('id')
	else:
		last_record = None
	actual_time = datetime.datetime.today()

	def get_context_data(self, **kwargs):
		context = super(TodayView, self).get_context_data(**kwargs)
		context["today"] = self.actual_time
		return context


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
