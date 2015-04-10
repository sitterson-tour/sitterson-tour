from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from tour.views import HomePageView

from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    url(r'^$', HomePageView.as_view()),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
	url(r'^contact/', TemplateView.as_view(template_name="contact.html")),
	url(r'^stops/', TemplateView.as_view(template_name="tour-stops.html")),
    url(r'^index/', TemplateView.as_view(template_name="index.html")),
)
