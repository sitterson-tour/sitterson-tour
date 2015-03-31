from django.http import HttpResponse
from django.views.generic import TemplateView
from django.conf.urls import patterns

class HomeView(TemplateView):
	template_name = "home.html"
	
