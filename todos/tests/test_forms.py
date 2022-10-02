from datetime import date
from http import HTTPStatus

from django.urls import reverse

from .base_testcase import ToDoBaseTestCase
from ..models import ToDo, User


class TodoFormsTestCase(ToDoBaseTestCase):

    def test_auth_user_can_create_todo_item(self):
        form_data = {
            'text': 'Какое-то тестовое задание',
            'finished_at': date(2022, 10, 4)
        }

        response = self.auth_client.post(
            reverse('todos:add'),
            data=form_data,
            follow=True
        )

        self.assertEqual(ToDo.objects.count(), 1)
        self.assertRedirects(response, reverse("todos:index"))

        todo = ToDo.objects.first()
        self.assertEqual(todo.text, form_data['text'])
        self.assertEqual(todo.finished_at, form_data['finished_at'])
        self.assertEqual(todo.author, self.user)

    def test_unath_user_cannot_create_todo_item(self):
        form_data = {
            'text': 'Какое-то тестовое задание',
            'finished_at': date(2022, 10, 4)
        }

        response = self.client.post(
            reverse("todos:add"),
            data=form_data,
            follow=True
        )

        self.assertEqual(ToDo.objects.count(), 0)
        self.assertEqual(response.status_code, HTTPStatus.NOT_FOUND)
