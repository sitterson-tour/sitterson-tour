from django.test import TestCase
from django.http import HttpRequest
from django.test import RequestFactory
from .views import tour_home_view, tour_stop_view


class HomePageViewTest(TestCase):

    def test_home_page_returns_correct_html(self):
        request = RequestFactory().get('/')
        response = tour_home_view(request)
        self.assertEqual(response.status_code, 200)




