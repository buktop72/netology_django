from django.core.validators import MinValueValidator
from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=60, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return f'{self.id} - {self.title} - {self.description}'

    class Meta:  # отображение моделей в админке
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Stock(models.Model):

    address = models.CharField(max_length=200, unique=True)
    products = models.ManyToManyField(
        Product,
        through='StockProduct',
        related_name='stocks',
    )

    def __str__(self):

        return f'{self.id} - {self.address}'

    class Meta:  # отображение моделей в админке
        verbose_name = 'Склад'
        verbose_name_plural = 'Склады'


class StockProduct(models.Model):

    stock = models.ForeignKey(
        Stock,
        on_delete=models.CASCADE,
        related_name='positions',
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='positions',
    )
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(
        max_digits=18,
        decimal_places=2,
        validators=[MinValueValidator(0)],  # Валидация, цена всегда положительная
    )

    def __str__(self):
        return f'{self.stock} - {self.product} - {self.quantity} кг. - {self.price} руб.'

    class Meta:  # отображение моделей в админке
        verbose_name = 'Продукты на складе'
        verbose_name_plural = 'Продукты на складах'
