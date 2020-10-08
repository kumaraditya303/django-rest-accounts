"""
    Tests for accounts app.
"""

from datetime import datetime

from django.contrib.auth import get_user_model
from django.test import TestCase


class UserModelTests(TestCase):
    """
    Tests for User Model where email is the unique identifiers
    for authentication instead of usernames.
    """

    def test_create_user(self):
        """
        Test for creating a normal user.
        """
        User = get_user_model()
        user = User.objects.create_user(
            email="normal@user.com", password="foo", dob=datetime.now().date()
        )
        self.assertEqual(user.email, "normal@user.com")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        self.assertIsNone(user.username)
        self.assertIsNotNone(user.dob)
        with self.assertRaises(TypeError):
            User.objects.create_user()
        with self.assertRaises(TypeError):
            User.objects.create_user(email="")
        with self.assertRaises(ValueError):
            User.objects.create_user(email="", password="foo")

    def test_create_superuser(self):
        """
        Test for creating a super user.
        """
        User = get_user_model()
        admin_user = User.objects.create_superuser("super@user.com", "foo")
        self.assertEqual(admin_user.email, "super@user.com")
        self.assertEqual(admin_user.__str__(), "super@user.com")
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
        self.assertIsNone(admin_user.username)
        with self.assertRaises(ValueError):
            User.objects.create_superuser(
                email="super@user.com", password="foo", is_superuser=False
            )
        with self.assertRaises(ValueError):
            User.objects.create_superuser(
                email="super@user.com", password="foo", is_staff=False
            )
