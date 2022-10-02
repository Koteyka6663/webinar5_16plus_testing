from django.test import Client, TestCase

from ..models import User


class ToDoBaseTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = User.objects.create_user(username='auth_user')

    def setUp(self):
        self.auth_client = Client()
        self.auth_client.force_login(self.user)
