from django.urls import reverse, path
from rest_framework.test import APITestCase
from rest_framework import status
from authors.apps.authentication.models import User


class Authentication(APITestCase):

    def test_for_new_user(self):
         # url = reverse('signup')
        data = {"user": {"username": "akram",
                         "email": "akram@gmail.com", "password": "Akram@mukasa2"}}
        response = self.client.post('/api/users/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
   
    def test_for_missing_username(self):
        """
        Method for testing if there is a missing username during registration.
        """
        data = {"user": { "username":"", "email": "akram@gmail.com", "password":"Akram@mukasa2"}}
        response = self.client.post('/api/users/' ,data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("Please the username should be at least 4 characters long and above", str(response.data))

    def test_for_missing_email(self):
        """
        Method for testing if there is a missing email during registration.
        """
        data = {"user": { "username":"mukasa", "email": "", "password":"Akram@mukasa2"}}
        response = self.client.post('/api/users/' ,data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("Please enter a valid email address", str(response.data))

    def test_login(self):
        # url = reverse('signup')
        data = {"user": {"username": "akram",
                         "email": "akram@gmail.com", "password": "Akram@mukasa2"}}
        response = self.client.post('/api/users/', data, format='json')
        # url = reverse('login')
        data = {"user": {"email": "akram@gmail.com", "password": "Akram@mukasa2"}}
        response = self.client.post('/api/users/login/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(User.objects.get().email, "akram@gmail.com")

    def test_login_with_non_existing_user(self):
        data = {"user": { "email": "akram@gmail.com", "password":"Akram@mukasa2"}}
        response = self.client.post('/api/users/login/',data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("A user with this email and password was not found.", str(response.data))
