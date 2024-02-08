import json
from django.test import TestCase, Client
from django.urls import reverse
from saas_app.users.models import User


class BaseUserTestCase(TestCase):
    def setUp(self):
        # Assuming `make_user` is a helper method to create a user instance
        # If not, replace this with the appropriate User creation logic
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='password')
        self.client = Client()

    def login(self):
        self.client.force_login(self.user)


class CurrentUserViewTestCase(BaseUserTestCase):

    url = reverse("api:v1:user")  # Moved reverse call to class attribute for optimization

    def test_needs_login(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 403)

    def test_get(self):
        self.login()
        response = self.client.get(self.url)
        data = json.loads(response.content.decode("utf-8"))
        self.assertEqual(data["email"], self.user.email)

    def test_put_valid(self):
        self.login()
        response = self.client.put(self.url, {"name": "foo"}, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        user = User.objects.get(pk=self.user.pk)
        self.assertEqual(user.name, "foo")

    def test_put_invalid(self):
        self.login()
        response = self.client.put(self.url, {}, content_type='application/json')
        self.assertEqual(response.status_code, 400)
