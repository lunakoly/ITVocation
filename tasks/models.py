from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

STATUS = (
    (0, "Свободно"),
    (1, "Занято"),
    (2, "Завершено")
)


class Task(models.Model):
    """
    Task model
    """
    # Ссылка на объект пользователя
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Название испытания
    header = models.CharField(max_length=50, blank=True)
    # текстовое описание
    text = models.CharField(max_length=2000, blank=True)
    # Ссыль на мероприятие
    link = models.CharField(max_length=500, blank=True)
    avatar = models.ImageField(upload_to="pictures", default="tasks/static/images/unknown.png")
    # Количество exp за выполнение
    exp = models.IntegerField(default=100)
    # Статус выполнения задачи
    status = models.IntegerField(choices=STATUS, default=0)
    # Дата публикации
    published = models.DateTimeField(default=timezone.now)

