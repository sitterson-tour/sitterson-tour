from django.test import TestCase
from django.http import HttpRequest
from django.test import RequestFactory
from .views import tour_home_view, contact_view, about_view, map_view
from .models import Stop


class HomePageViewTest(TestCase):

    def test_home_page_response(self):
        request = RequestFactory().get('/')
        response = tour_home_view(request)
        self.assertEqual(response.status_code, 200)

class ContactViewTest(TestCase):

	def test_contact_page_response(self):
		request = RequestFactory().get('/contact/')
		response = contact_view(request)
		self.assertEqual(response.status_code, 200)

class AboutViewTest(TestCase):

	def test_contact_page_response(self):
		request = RequestFactory().get('/about/')
		response = about_view(request)
		self.assertEqual(response.status_code, 200)		

class MapViewTest(TestCase):

	def test_contact_page_response(self):
		request = RequestFactory().get('/map/')
		response = map_view(request)
		self.assertEqual(response.status_code, 200)		

class StopModelTest(TestCase):

	def create_stop(self):
		return Stop.objects.create(title='title', subtitle='subtitle', content='content', slug='title', description='description')

	def test_stop_model(self):
		stop = self.create_stop()
		self.assertTrue(isinstance(stop, Stop))
		self.assertEqual(stop.__unicode__(), stop.title)
		self.assertEqual(stop.url(), 'http://tour.cs.unc.edu/stop/title/')





