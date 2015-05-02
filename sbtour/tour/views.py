from django.http import HttpResponse
from django.views.generic import TemplateView
from django.conf.urls import patterns
from django.shortcuts import render
from .models import Stop


def tour_home_view(request, *args, **kwargs):
	stop_list = Stop.objects.filter(published=True)
	template_name = 'index.html'
	context = { 
		'stop_list': stop_list
	}
	return render(request, template_name, context)

def tour_stop_view(request, stop_slug):
	stop = Stop.objects.get(slug=stop_slug, published=True)
	template_name = 'stop.html'
	context = {
		'stop': stop
	}
	return render(request, template_name, context)

def contact_view(request, *args, **kwargs):
	template_name = 'contact.html'
	return render(request, template_name)	

def about_view(request, *args, **kwargs):
	template_name = 'about.html'
	return render(request, template_name)	

def map_view(request, *args, **kwargs):
	template_name = 'map.html'
	return render(request, template_name)	
