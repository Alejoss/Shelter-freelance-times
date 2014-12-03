from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.http import Http404

from rest_framework import generics, permissions

from activities.models import TrophySet
from shelter.serializers import TrophySerializer
from shelter.permissions import IsOwnerReadOnly


def logout_user(request):
	logout(request)
	return redirect('activities:login')


def login_user(request):
	if request.method == "POST":
		username = request.POST["username"]
		password = request.POST["password"]
		user = authenticate(username=username, password=password)

		if user is not None:
			login(request, user)
			return redirect('times:today')
		else:
			raise Http404

	else:
		return render(request, 'activities/login.html')


class TrophyAPIListView(generics.ListCreateAPIView):

	queryset = TrophySet.objects.all()
	serializer_class = TrophySerializer
	permissions_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerReadOnly,)


class TrophyAPIDetailView(generics.RetrieveUpdateDestroyAPIView):

	queryset = TrophySet.objects.all()
	serializer_class = TrophySerializer
	permissions_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerReadOnly,)
