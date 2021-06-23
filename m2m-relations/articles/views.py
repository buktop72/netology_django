from django.shortcuts import render

from articles.models import Article


# def articles_list(request):
#     template = 'articles/news.html'
#     context = {}
#
#     # используйте этот параметр для упорядочивания результатов
#     # https://docs.djangoproject.com/en/3.1/ref/models/querysets/#django.db.models.query.QuerySet.order_by
#     ordering = '-published_at'
#
#     return render(request, template, context)

def articles_list(request):
    template = 'articles/news.html'
    ordering = '-published_at'
    article1 = Article.objects.all().prefetch_related('tags').order_by(ordering)
    print(type(article1))
    content = {'object_list': article1}

    return render(request, template, context=content)


