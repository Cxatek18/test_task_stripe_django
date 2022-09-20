from django.db import models


class Item(models.Model):

    CURRENCY_ITEM = [
        ('USD', 'usd'),
        ('AUD', 'aud'),
    ]

    name = models.CharField(
        verbose_name='Название товара',
        max_length=255,
    )
    description = models.TextField(
        verbose_name='Описание',
        blank=True,
    )
    price = models.PositiveIntegerField(
        verbose_name='Цена',
        default=0
    )
    currency = models.CharField(
        verbose_name='Валюта',
        choices=CURRENCY_ITEM,
        default='USD',
        max_length=50,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Items'


class Order(models.Model):
    items_in_order = models.ManyToManyField(
        'Item',
        verbose_name='Список товаров',
        related_name='items_in_order',
    )
    order_discount = models.ForeignKey(
        'Discount',
        null=True,
        blank=True,
        on_delete=models.CASCADE
    )
    order_tax = models.ForeignKey(
        'Tax',
        null=True,
        blank=True,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'


class Discount(models.Model):
    discount = models.PositiveIntegerField(
        verbose_name='скидка',
        default=0
    )

    def __str__(self):
        return str(self.discount)

    class Meta:
        verbose_name = 'Discount'
        verbose_name_plural = 'Discounts'


class Tax(models.Model):
    tax = models.PositiveIntegerField(
        verbose_name='налог',
        default=0
    )

    def __str__(self):
        return str(self.tax)

    class Meta:
        verbose_name = 'Tax'
        verbose_name_plural = 'Taxs'
