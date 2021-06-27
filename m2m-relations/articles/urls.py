from django.urls import path
from articles.views import ArticleList

urlpatterns = [
    path('', ArticleList.as_view(), name='articles'),  # привязка класса представления к текущему маршруту
]
