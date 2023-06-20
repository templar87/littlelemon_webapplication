from django.test import SimpleTestCase, RequestFactory, TestCase
from django.urls import reverse, resolve
from Restaurant.views import index, MenuItemView, SingleMenuItemView

# use SimpleTestCase when you don't need to interact with database

class TestUrls(SimpleTestCase):
    def test_index_url_is_resolved(self):
        url = reverse('index')
        print(resolve(url))
        self.assertEquals(resolve(url).func, index)
    #MenuItemView is class based.  Therefore, need to change func to func.view_class
    def test_MenuItemView_url_is_resolved(self):
        url = reverse('item')
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, MenuItemView)
        
    def test_SingleMenuItemView_url_is_resolved(self):
        url = reverse('singleitem', args=[1])
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, SingleMenuItemView)
    
   