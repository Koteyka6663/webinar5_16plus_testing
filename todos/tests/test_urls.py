from http import HTTPStatus

from .base_testcase import ToDoBaseTestCase


class ToDoUrlsTestCase(ToDoBaseTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.public_url = ('/', 'todos/index.html')
        cls.private_url = ('/add/', 'todos/add.html')

    def test_public_urls_works(self):
        url, template = self.public_url
        response = self.client.get(url)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, template)

    def test_private_urls_works(self):
        url, template = self.private_url
        response = self.auth_client.get(url)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, template)

    def test_404_page(self):
        response = self.client.get("/unexpected_page/")
        self.assertEqual(response.status_code, HTTPStatus.NOT_FOUND)

    def test_unauth_user_cannot_access_private_url(self):
        url, _ = self.private_url
        response = self.client.get(url)
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
