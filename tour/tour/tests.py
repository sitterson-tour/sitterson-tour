from django.test import TestCase
from django.http import HttpRequest
from tour.views import HomePageView
from django.test import RequestFactory


class HomePageViewTest(TestCase):

    def test_home_page_returns_correct_html(self):
        request = RequestFactory().get('/')
        view = HomePageView.as_view(template_name='home.html')
        
        response = view(request)
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.template_name[0], 'home.html')
