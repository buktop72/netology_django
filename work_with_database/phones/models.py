from django.db import models


class Phone(models.Model):  # создаем таблицу Phone
    name = models.TextField()
    price = models.FloatField()
    image = models.ImageField()
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField()  #


    def __str__(self):  # строковое представление моделей

        return (f'{self.name}-{self.price}-{self.image}-{self.release_date}-{self.lte_exists}-{self.slug}')