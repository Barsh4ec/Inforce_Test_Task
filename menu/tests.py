from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from restaurant.models import Restaurant
from menu.models import Menu


class MenuTests(APITestCase):
    def setUp(self):
        Restaurant.objects.create(name='Restaurant #1', address='example address')
        Restaurant.objects.create(name='Restaurant #2', address='example address2')

    def test_menu_create(self):
        url = reverse('add-menu')
        data = {'restaurant': 1, 'items': 'example items'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Menu.objects.count(), 1)

    def test_menu_get(self):
        response = self.client.get(reverse('get-menu'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)