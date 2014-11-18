from django.conf.urls import patterns, url

from activities import views

urlpatterns = patterns('',
						url(r'^api/trophy_list/$', views.TrophyAPIListView.as_view(), name = 'api_trophy_list'),
						url(r'^api/trophy/(?P<pk>[0-9]+)/$', views.TrophyAPIListView.as_view(), name = 'api_trophy_list')
					)
