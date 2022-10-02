from datetime import date
from http import HTTPStatus

from django.urls import reverse

from .base_testcase import ToDoBaseTestCase
from ..forms import ToDoForm
from ..models import ToDo


class ToDoViewsTestCase(ToDoBaseTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.todo = ToDo.objects.create(
            text="Тестовое задание",
            finished_at=date(2022, 10, 5),
            author=cls.user
        )

        cls.public_url = (reverse('todos:index'), 'todos/index.html')
        cls.private_url = (reverse('todos:add'), 'todos/add.html')

    def test_correct_templates_used_for_all_reversed_urls(self):
        urls = (self.private_url, self.public_url)
        for url, template in urls:
            with self.subTest(url=url):
                response = self.auth_client.get(url)
                self.assertEqual(response.status_code, HTTPStatus.OK)
                self.assertTemplateUsed(response, template)

    def test_index_page_context_is_correct(self):
        url, _ = self.public_url
        response = self.client.get(url)
        self.assertIn('todos', response.context)
        todo = response.context['todos'][0]
        self.assertEqual(todo.text, self.todo.text)
        self.assertEqual(todo.author, self.todo.author)
        self.assertEqual(todo.finished_at, self.todo.finished_at)

    def test_add_page_context_is_correct(self):
        url, _ = self.private_url
        response = self.auth_client.get(url)
        self.assertIn('form', response.context)
        self.assertIsInstance(response.context['form'], ToDoForm)
