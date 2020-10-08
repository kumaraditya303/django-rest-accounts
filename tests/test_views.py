"""
    Tests for accounts app.
"""

from datetime import datetime
from io import BytesIO

from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
from django.shortcuts import reverse
from django.test import TestCase
from PIL import Image
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase


class UserViewTests(APITestCase):
    """
    Tests for User Views for user registration, login and logout.
    """

    def setUp(self):
        """
        Setup function to create a image.
        """
        file = BytesIO()
        image = Image.new("RGB", size=(100, 100), color=(155, 0, 0))
        image.save(file, "jpeg")
        file.name = "test.jpeg"
        file.seek(0)
        self.image = SimpleUploadedFile(
            name="test.jpeg", content=file.read(), content_type="image/jpeg"
        )

    def test_register(self):
        """
        Test for user registration.
        """
        User = get_user_model()
        response = self.client.post(
            reverse("register"),
            {
                "first_name": "test",
                "last_name": "user",
                "email": "test@test.com",
                "password": "foobar",
                "dob": datetime.now().date(),
                "image": self.image,
            },
            format="multipart",
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().email, "test@test.com")
        self.assertTrue(User.objects.get().is_active)
        self.assertFalse(User.objects.get().is_staff)
        self.assertFalse(User.objects.get().is_superuser)
        response = self.client.post(
            reverse("register"),
            {
                "first_name": "test",
                "last_name": "user",
                "email": "test@test.com",
                "password": "foobar",
            },
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertNotEqual(User.objects.count(), 2)
        response = self.client.post(
            reverse("register"), {"email": "", "password": "foobar"}
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertNotEqual(User.objects.count(), 2)
        response = self.client.post(
            reverse("register"), {"email": "test@test.com", "password": ""}
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertNotEqual(User.objects.count(), 2)

    def test_login(self):
        """
        Test for user login.
        """
        User = get_user_model()
        self.test_register()
        response = self.client.post(
            reverse("login"), {"username": "test@test.com", "password": "foobar"}
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Token.objects.count(), 1)
        self.assertEqual(Token.objects.get().key, User.objects.get().auth_token.key)
        self.assertEqual(Token.objects.get().key, response.data["token"])
        response = self.client.post(
            reverse("login"), {"username": "falsetest@test.com", "password": "foo"}
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertNotEqual(Token.objects.count(), 2)

    def test_logout(self):
        """
        Test for user logout.
        """
        self.test_login()
        User = get_user_model()
        response = self.client.get(reverse("logout"))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(Token.objects.count(), 1)
        self.client.credentials(
            HTTP_AUTHORIZATION=f"Token {User.objects.get().auth_token.key}"
        )
        response = self.client.get(reverse("logout"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertNotEqual(Token.objects.count(), 1)
