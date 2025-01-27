from rest_framework import status
from rest_framework.test import APITestCase

# endpoints to test:
# /auth/register/
# /auth/token/
# /auth/refresh/

# test cases:
# 1. test user registration
# 2. test token pair obtain
# 3. test token refresh
# 4. test token pair obtain with invalid credentials
# 5. test token refresh with invalid token


class UserAuthTest(APITestCase):
    def setUp(self):
        self.register_url = "http://127.0.0.1:8000/api/auth/register/"
        self.token_url = "http://127.0.0.1:8000/api/auth/token/"
        self.refresh_url = "http://127.0.0.1:8000/api/auth/token/refresh/"

        self.user_data = {
            "email": "dummy@gmail.com",
            "username": "dummy",
            "password": "Dummy@123",
        }

        self.client.post(self.register_url, self.user_data)

    def test_user_registration_duplicate_uname(self):
        response = self.client.post(self.register_url, self.user_data)
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertFalse(response.data["success"])
        self.assertIn("error", response.data)
        self.assertIn(
            "A user with that username already exists.",
            response.data["error"]["username"],
        )

    def test_token_pair_obtain(self):
        response = self.client.post(
            self.token_url,
            {
                "username": self.user_data["username"],
                "password": self.user_data["password"],
            },
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data["success"])
        self.assertIn("access", response.data["data"])
        self.assertIn("refresh", response.data["data"])

    def test_token_refresh(self):
        token_response = self.client.post(
            self.token_url,
            {
                "username": self.user_data["username"],
                "password": self.user_data["password"],
            },
        )
        refresh_token = token_response.data["data"]["refresh"]

        response = self.client.post(self.refresh_url, {"refresh": refresh_token})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data["success"])
        self.assertIn("access", response.data["data"])

    def test_invalid_token_pair_obtain(self):
        response = self.client.post(
            self.token_url, {"username": "dummy", "password": "wrongpassword"}
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertFalse(response.data["success"])
        self.assertIn("error", response.data)

    def test_invalid_token_refresh(self):
        response = self.client.post(self.refresh_url, {"refresh": "invalid_token"})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertFalse(response.data["success"])
        self.assertIn("error", response.data)
