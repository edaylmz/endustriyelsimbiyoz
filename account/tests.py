from django.test import TestCase,Client
from django.test import TestCase
from django.urls import resolve

from account.views import account_anasayfa

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('account/')
        self.assertEqual(found.func, account_anasayfa)



# Create your tests here.
