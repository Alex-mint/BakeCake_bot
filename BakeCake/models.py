from django.db import models


CHOICES = (
    (None,'Готовим ваш торт'),
    (False,'Торт в пути'),
    (True,'Торт у вас')
)

class Profile(models.Model):
    external_id = models.PositiveIntegerField(
        verbose_name='ID пользователя в сети',
        unique=True
    )
    name = models.TextField(
        'Псевдоним',
    )
    first_name = models.TextField(
        'Имя пользователя',
        blank=True
    )
    last_name = models.TextField(
        'Фамилия пользователя',
        blank=True
    )

    def __str__(self):
        #return f'#{self.external_id} {self.name}'
        return self.name
    class Meta:#нужен для добавления информации к нашим моделям
        verbose_name='Профиль'
        verbose_name_plural = 'Профили'


class Message(models.Model):
    profile = models.ForeignKey(
        'Profile',
        verbose_name='Профиль',
        on_delete=models.PROTECT,
    )

    text = models.TextField(
        'Текст'
    )
    created_at = models.DateTimeField(
        'Время получения',
        auto_now_add=True
    )
    order_status = models.BooleanField(
        'Статус заказа',
        choices=CHOICES,
        null=True)
    number_levels = models.TextField('Количество уровней',blank=True)
    form = models.TextField('Форма',blank=True)
    topping = models.TextField('Топпинг',blank=True)
    berries = models.TextField('Ягоды',blank=True)
    decor = models.TextField('Декор',blank=True)
    title = models.TextField('Надпись',blank=True)


    def __str__(self):
        return f'Заказ {self.pk} от {self.profile}'

    class Meta:
        verbose_name = 'Заказы'
        verbose_name_plural = 'Заказы'

