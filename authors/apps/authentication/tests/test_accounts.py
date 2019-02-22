from rest_framework import serializers, status
from rest_framework.test import APITestCase
from ..backends import JWTAuthentication
from ..models import User


class AccountTestCase(APITestCase):

    def test_recieve_a_token_after_registration(self):
        data = {
            "user": {
            "username": "akram",
            "email": "mukasaakram@gmail.com",
            "password": "Akram@2011"
            }
        }
        response = self.client.post('/api/users/', data,format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        assert 'token' in response.data

    def test_token_received_after_successful_login(self):
        """
        Test that a user will receive 
        a token after successfull login
        """
        data = {
            "user": {
            "username": "akram",
            "email": "mukasaakram@gmail.com",
            "password": "Akram@2011"
            }
        }
        response = self.client.post('/api/users/',data, format='json')
        data = {"user": { "email": "mukasaakram@gmail.com", "password":"Akram@2011"}}
        response = self.client.post('/api/users/login/',data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK) 
        assert 'token' in response.data

    def test_user_can_get_token_for_current_user(self):
        """
        Test that a user will receive 
        a token after successfull login
        """
        data = {
            "user": {
            "username": "akram",
            "email": "mukasaakram@gmail.com",
            "password": "Akram@2011"
            }
        }
        response = self.client.post('/api/users/',data, format='json')
        data = {
            "user": {
            "email": "mukasaakram@gmail.com",
            "password": "Akram@2011"
            }
        }
        response = self.client.post('/api/users/login/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK) 
        assert 'token' in response.data
        self.client.credentials(HTTP_AUTHORIZATION= 'Bearer ' + response.data['token'])
        response = self.client.get('/api/user/', format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)   

    # def test_wrong_token_header_prefix(self):
    #     """
    #     Test when wrong authoriation header
    #     prefix is entered
    #     """
    #     self.client.credentials(HTTP_AUTHORIZATION= 'hgfds ' + 'poiuytfd')
    #     response = self.client.get("/api/user/", format="json")
    #     self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_for_invalid_token(self):
        """
        Test when an invalid 
        authorisation header is provided
        """
        self.client.credentials(HTTP_AUTHORIZATION= 'Token ' + 'yyuug')
        response = self.client.get("/api/user/", format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)  

    def test_no_token_in_header(self):
        """
        Test when no authorization token
        is entered in the header
        """
        self.client.credentials(HTTP_AUTHORIZATION= ' ' + 'shfdj')
        response = self.client.get("/api/user/", format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN) 