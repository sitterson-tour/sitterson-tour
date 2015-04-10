from django.test import TestCase
from django.http import HttpRequest
from tour.views import HomePageView, TourStopView
from django.test import RequestFactory


class HomePageViewTest(TestCase):

    def test_home_page_returns_correct_html(self):
        request = RequestFactory().get('/')
        view = HomePageView.as_view(template_name='index.html')
        
        response = view(request)
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.template_name[0], 'index.html')


class TourStopViewTest(TestCase):

    def test_tour_stop_page(self):
        request = RequestFactory().get('/stops/')
        view = TourStopView.as_view(template_name='stop.html')

        response = view(request)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.template_name[0], 'stop.html')

