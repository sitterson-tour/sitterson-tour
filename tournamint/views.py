from django.http import HttpResponse

def home(request):
	html = "<html><h2>Home</h2></html>"
	return HttpResponse(html)
	
