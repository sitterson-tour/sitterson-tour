from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView


from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'stops.views.tour_home_view', name='home'),	 
    url(r'^admin/', include(admin.site.urls)),
	url(r'^stop/(?P<stop_slug>(\w|-)+)/$', 'stops.views.tour_stop_view', name='stop'),
    url(r'^about/', 'stops.views.about_view', name='about'),	 
    url(r'^contact/', 'stops.views.contact_view', name='contact'),	 
    url(r'^map/', 'stops.views.map_view', name='map'),	 
)
