from django.test import Client, TestCase
from django.urls import reverse

from rest_framework import status

from Restaurant.models import Menu

# Create your tests here.
class MenuViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.item_url = reverse('item')
        
    
    def test_getall(self):
        response = self.client.get(self.item_url)
        self.assertEquals(response.status_code, 200)