from django.test import TestCase
from Restaurant.models import Menu
        
# Create your tests here.
class MenuTest(TestCase):
    def setUp(self):
        self.item = Menu.objects.create(
            ID = 3,
            Title = "IceCream",
            Price = 80,
            Inventory = 100
        )
        
    def test_get_item(self):
        item = f'{self.item.Title}:{self.item.Price}'
        self.assertIsInstance(self.item.Price, int)
        self.assertEqual(item, "IceCream:80")