from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    url(r'^$', TemplateView.as_view(template_name="home.html")),
	url(r'^contact/', TemplateView.as_view(template_name="contact.html")),
	url(r'^stops/', TemplateView.as_view(template_name="tour-stops.html")),
	url(r'^admin/', include(admin.site.urls)),


)
