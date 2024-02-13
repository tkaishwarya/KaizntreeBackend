from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User

from rest_framework.authtoken.models import Token

class ItemTestCase(APITestCase):
    def setUp(self):
        # Create a user
        self.user = User.objects.create_user(username='testuser', password='password123')
        # Generate token for the user
        self.token = Token.objects.create(user=self.user)
        # Include token in the request headers
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token}')

    def test_create_item(self):
        url = reverse('item-list')
        data = {'name': 'Test Item', 'stock_status': True, 'available_stock': 10}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_items(self):
        url = reverse('item-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


