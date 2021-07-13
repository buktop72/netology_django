from rest_framework import serializers
from logistic.models import Product, Stock, StockProduct


class ProductSerializer(serializers.ModelSerializer):
    # сериализатор для продукта
    class Meta:
        model = Product
        fields = ['id', 'title', 'description']


class ProductPositionSerializer(serializers.ModelSerializer):
    # сериализатор для позиции продукта на складе

    class Meta:
        model = StockProduct
        fields = ['product', 'quantity', 'price']


class StockSerializer(serializers.ModelSerializer):
    positions = ProductPositionSerializer(many=True)

    # сериализатор для склада
    class Meta:
        model = Stock
        fields = ['address', 'positions']

    def create(self, validated_data):
        # достаем связанные данные для других таблиц
        # positions - Список словарей OrderedDict с ключами: 'product', 'quanty', 'price'
        positions = validated_data.pop('positions')

        # создаем склад по его параметрам
        stock = super().create(validated_data)   # stock: 14 - Чебоксары

        # заполняем связанные таблицы, в нашем случае: таблицу StockProduct
        # с помощью списка positions
        for item in positions:  # item: OrderedDict
            # передаем в ф-ю 'update_or_create' id создавемого cклада и продукты(OrderedDict)
            StockProduct.objects.update_or_create(stock=stock, **item)
        return stock

    def update(self, instance, validated_data):
        # достаем связанные данные для других таблиц
        positions = validated_data.pop('positions')

        # обновляем склад по его параметрам
        stock = super().update(instance, validated_data)

        # обновляем связанные таблицы, в нашем случае: таблицу StockProduct
        # с помощью списка positions

        # удаляем устаревшие данные о продуктах на складе
        stock.positions.all().delete()

        # Добавляем новые данные о продукта на складе
        for item in positions:
            StockProduct.objects.update_or_create(stock=stock, **item)
        return stock


