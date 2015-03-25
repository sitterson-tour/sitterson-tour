from django.http import HttpResponse

def home(request):
	html = "<html><h2>Tournamint</h2></html>"
	return HttpResponse(html)
	
