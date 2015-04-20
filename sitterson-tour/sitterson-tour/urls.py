from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from tour.views import HomePageView

from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'tour.views.tour_home_view', name='home'),	 
    url(r'^admin/', include(admin.site.urls)),
	url(r'^contact/', TemplateView.as_view(template_name="contact.html")),
	url(r'^stops/', TemplateView.as_view(template_name="stop.html")),
	url(r'^stop/(?P<stop_slug>\w+)/$', 'tour.views.tour_stop_view', name='stop'),	 
    url(r'^index/', TemplateView.as_view(template_name="index.html")),
)
