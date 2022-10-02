from datetime import date

from django.conf import settings
from django.test import TestCase

from ..models import ToDo, User


class ToDoModelsTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='user')
        self.todo = ToDo.objects.create(
            text="Какой-то тестовый текст",
            finished_at=date(2022, 10, 4),
            author=self.user
        )

    def test_model_have_correct_object_name(self):
        expected_object_name = settings.TODO_OUTPUT_TEMPLATE.format(self.todo.text, self.todo.finished_at)
        self.assertEqual(expected_object_name, str(self.todo))
