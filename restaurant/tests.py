from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from restaurant.models import Restaurant


class RestaurantTests(APITestCase):
    def setUp(self):
        Restaurant.objects.create(name='Restaurant #1', address='example address')
        Restaurant.objects.create(name='Restaurant #2', address='example address2')

    def test_restaurant_create(self):
        url = reverse('create-restaurants')
        data = {'name': 'Restaurant #3', 'address': 'example address3'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Restaurant.objects.count(), 3)

    def test_restaurant_get(self):
        response = self.client.get(reverse('get-restaurants'))
        self.assertTrue({'id': 8, 'name': 'Restaurant #1', 'address': 'example address'} in response.data)