from django.conf.urls import patterns, url

from times import views

urlpatterns = patterns('',
					# Today app
                       url(r'^today/$', views.TodayView.as_view(), name='today'),
                       url(r'^start/$', views.StartApiView.as_view(), name='start'),
                       url(r'^stop/$', views.StopApiView.as_view(), name='stop'),
                       url(r'^record/(?P<pk>[0-9]+)/$', views.RecordApiView.as_view(), name='record'),
					# Overview app
                       url(r'^overview/$', views.DayListView.as_view(), name='overview'),
                       url(r'^overview/weeks$', views.DayListView.as_view(), name='overview'),

                       url(r'^api/week_list/$', views.WeekListApiView.as_view(), name='api_weeklist'),
                  	   url(r'^api/day_list/$', views.DayListApiView.as_view(), name='api_daylist'),
                  	   url(r'^api/day/(?P<pk>[0-9]+)$', views.DayApiView.as_view(), name='api_daydetail'),
                  	   url(r'^users/$', views.UserApiListView.as_view(), name='api_userlist'),
                  	   url(r'^users/(?P<pk>[0-9]+)/$', views.UserApiDetailView.as_view(), name='api_userdetail')
                       )
