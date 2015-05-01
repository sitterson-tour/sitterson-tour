from django.http import HttpResponse
from django.views.generic import TemplateView
from django.conf.urls import patterns
from django.shortcuts import render
from .models import TourStop


class HomePageView(TemplateView):
    template_name = "index.html"

class TourStopView(TemplateView):
    template_name = "stop.html"

def tour_home_view(request, *args, **kwargs):
	stop_list = TourStop.objects.filter(published=True)
	template_name = 'index.html'

	context = { 
		'stop_list': stop_list
	}

	return render(request, template_name, context)

def tour_stop_view(request, stop_slug):
	stop = TourStop.objects.get(slug=stop_slug, published=True)
	template_name = 'stops.html'

	context = {
		'stop': stop
	}

	return render(request, template_name, context)
	
