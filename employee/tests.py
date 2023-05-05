from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from employee.models import Employee


class EmployeeTests(APITestCase):

    def test_employee_create(self):
        url = reverse('add-employee')
        data = {'name': 'employee1', 'surname': 'example'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Employee.objects.count(), 1)

    def test_employee_get(self):
        response = self.client.get(reverse('get-employee'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
