from django.views.generic import ListView  # класс представления, создает список объектов из набора запросов
from articles.models import Article


class ArticleList(ListView):  # создаем  свой класс на основе ListView
	model = Article  # модель, с которой работает представление
	template_name = 'articles/news.html'  # шаблон
	ordering = '-published_at'  #  сортировка по дате

