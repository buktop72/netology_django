import csv
from phones.models import Phone
from django.core.management.base import BaseCommand
from django.template.defaultfilters import slugify

# записываем данные из csv в БД
class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for phone in phones:
            name = phone['name']
            price = float(phone['price'])
            image = phone['image']
            release_date = phone['release_date']
            lte_exists = phone['lte_exists']
            slug = slugify(name)
            db = Phone(name=name, price=price, image=image, release_date=release_date, lte_exists=lte_exists, slug=slug)
            db.save()
