from django.db import models
from django.contrib.auth import get_user_model
from django.utils.timezone import now
User = get_user_model()


class Request(models.Model):
    first_name = models.CharField(verbose_name='Имя', max_length=30)
    last_name = models.CharField(verbose_name='Фамилия', max_length=30)
    phone = models.CharField(verbose_name='Телефон', max_length=30)
    creation_date = models.DateTimeField(
        default=now, blank=True, verbose_name='Дата создания')
    address = models.CharField(verbose_name='Адрес', max_length=150)
    message = models.CharField(verbose_name='Сообщение', max_length=400)
    user = models.ForeignKey(
        User, verbose_name='Пользователь', on_delete=models.CASCADE)
    REQUEST_STATUS = (
        (1, 'Создана'),
        (2, 'Назначена'),
        (3, 'В работе'),
        (4, 'Выполнена'),
    )
    request_status = models.IntegerField(
        verbose_name='Статус заявки', choices=REQUEST_STATUS)

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'
