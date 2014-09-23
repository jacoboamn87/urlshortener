from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns(
    '',

    url(r'^', include('shorturls.urls', namespace='shorturls')),

    url(r'^admin/', include(admin.site.urls)),
)
