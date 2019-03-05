from authors.apps.authentication.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
# from .test_validation import AccountTests
from . import (user1, login1)


class PassordResetTests(APITestCase):
    """Handles user reseting password"""

    def test_reset_user_password(self):
        """
        test validates whether email exits the it sends password
        reset lint to that email
        """
        self.client.post("/api/users/", user1, format="json")
        self.client.post("/api/users/login/", login1, format="json")
        response = self.client.post(
            "/api/password-reset/",
            data={"user": {
                "email": " mukasaakram55@gmail.com"
            }},
            format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn(response.data['Message'],
                      "Please check your email a link has been sent to you")

    def test_confirm_reset_user_password_status_code(self):
        """
        test ckecks whether token is in the link the user has clicked
        on his mail
        """
        response = self.client.get(
            "/api/password-reset/eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9."
            "eyJpZCI6MiwiZW1haWwiOiJha3JhbS5tdWthc2"
            "FAYW5kZWxhLmNvbSIsImV4cCI6MTU1Mjk5MzY3MH0."
            "Y67AssFm_jngvbmZFVfcDJub8A6qUwe2jFriePP_TeQ"
            "/",
            format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        assert "token" in response.data

    # def test_confirm_reset_without_token(self):
    #     """
    #     Tests checks for return of error when user doesnt have token
    #     """
    #     response = self.client.put("/api/password/reset/done/")
    #     self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
    #     self.assertIn(
    #         response.data['detail'],
    #         "ErrorDetail(string='Authentication credentials were not provided.',"
    #         "code='not_authenticated')")

    # def test_confirm_reset(self):
    #     """"This method tests successful reseting of a user password"""

    #      self.password_update = {"user": {"password": "Newpaswd1"}}
    #     res = self.client.post("/api/users/", new_user, format="json")
    #     token = res.data['token']
    #     response = self.client.get("/api/password-reset/{}/".format(token))
    #     token = response.data['token']
    #     self.add_credentials(response.data['token'])
    #     response = self.client.put(
    #         "/api/password/reset/done/",
    #         data=self.password_update,
    #         format="json")
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertIn(response.data['Message'],
    #                   "Your password has been updated succesfully")
