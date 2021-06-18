from django.shortcuts import render
from pprint import pprint

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, кг': 0.3,
        'сыр, кг': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
}


dish_name = {
    'omlet': 'Омлет',
    'pasta': 'Паста',
    'buter': 'Бутерброд'
}


def recipes(request, dish):  # dish - часть URL
    servings = request.GET.get('servings')  # получаем количество персон (параметр запроса)
    recipe = DATA.get(dish, None)  # словарь с рецептом по ключу dish
    if dish in dish_name:
        dish_rus = dish_name[dish]  # переводим на русский
        dish = dish_rus
    if servings:
        dict_summ = {i: round(j*int(servings), 3) for i,j in recipe.items()}  # умножаем кол-во ингр-в на кол-во персон
        context = {'recipe': dict_summ, 'dish': dish, 'servings': servings}
    else:
        context = {'recipe': recipe, 'dish': dish, 'servings': 1}

    pprint(context)
    return render(request, 'calculator/index.html', context=context)  # передаем СЛОВАРЬ в шаблон calculator/index.html

