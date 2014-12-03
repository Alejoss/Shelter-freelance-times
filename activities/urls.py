from django.conf.urls import patterns, url

from activities import views

urlpatterns = patterns('',
						url(r'^logout/', views.logout_user, name='logout'),
						url(r'^login/', views.login_user, name='login'),
						url(r'^api/trophy_list/$', views.TrophyAPIListView.as_view(), name = 'api_trophy_list'),
						url(r'^api/trophy/(?P<pk>[0-9]+)/$', views.TrophyAPIListView.as_view(), name = 'api_trophy_list')
					)
