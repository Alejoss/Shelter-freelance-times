from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
     				url(r'^times/', include('times.urls', namespace="times")),
     				url(r'^act/', include('activities.urls', namespace="activities")),
				    url(r'^admin/', include(admin.site.urls)),
				    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
)
