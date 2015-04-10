from django.http import HttpResponse
from django.views.generic import TemplateView
from django.conf.urls import patterns


class HomePageView(TemplateView):
    template_name = "index.html"

class TourStopView(TemplateView):
    template_name = "stop.html"
	
