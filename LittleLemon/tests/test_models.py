from django.test import TestCase
from restaurant.models import Menu

#TestCase class
class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="Vanilla Ice Cream", price=3.50, inventory=100)
        self.assertEqual(item, "Vanilla Ice Cream : 3.50")