import unittest
from django.test import TestCase
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer
from django.http import response

class MenuViewTest(TestCase):

    def setUp(self):
        Menu.objects.create(name="Pizza", price=9.99, inventory=50)
        Menu.objects.create(name="Pasta", price=7.99, inventory=50)
        Menu.objects.create(name="Burger", price=5.99, inventory=50)

    def test_getall(self):
        menu_list = Menu.objects.all()
        serializer = MenuSerializer(menu_list, many=True)
        self.assertEqual(response.data, serializer.data)