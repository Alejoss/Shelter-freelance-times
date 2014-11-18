from rest_framework import generics, permissions

from activities.models import Activity, TrophySet
from shelter.serializers import TrophySerializer, ActivitySerializer
from shelter.permissions import IsOwnerReadOnly


class TrophyAPIListView(generics.ListCreateAPIView):
	
	queryset = TrophySet.objects.all()
	serializer_class = TrophySerializer
	permissions_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerReadOnly,)


class TrophyAPIDetailView(generics.RetrieveUpdateDestroyAPIView):

	queryset = TrophySet.objects.all()
	serializer_class = TrophySerializer
	permissions_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerReadOnly,)
