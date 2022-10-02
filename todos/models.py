from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class ToDo(models.Model):
    text = models.TextField(
        blank=False,
        verbose_name="Что нужно сделать?",
        help_text="Текст задачи"
    )
    added_at = models.DateTimeField(auto_now_add=True)
    finished_at = models.DateField(
        null=False,
        blank=False,
        verbose_name="Срок",
        help_text="Дата, когда задача станет неактуальной"
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"

    def __str__(self):
        return settings.TODO_OUTPUT_TEMPLATE.format(self.text, self.finished_at)
