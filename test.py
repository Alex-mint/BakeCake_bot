#from BakeCake.models import Profile, Order
#model = Flat.owned_by.through



#class Order(models.Model):
#    order = models.ForeignKey(
#        'Profile',
#        verbose_name = 'Профиль',
#        on_delete = models.PROTECT,
#    )
#
#    order_status = models.BooleanField(
#        'Статус заказа',
#        choices=CHOICES,
#        null=True)
#    number_levels = models.TextField('Количество уровней',blank=True)
#    form = models.TextField('Форма',blank=True)
#    topping = models.TextField('Топпинг',blank=True)
#    berries = models.TextField('Ягоды',blank=True)
#    decor = models.TextField('Декор',blank=True)
#    title = models.TextField('Надпись',blank=True)
#
#    def __str__(self):
#        return self.order
#
#    class Meta:
#        verbose_name = 'Заказы'
#        verbose_name_plural = 'Заказы'