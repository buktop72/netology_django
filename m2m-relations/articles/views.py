from django.shortcuts import render
from articles.models import Article


def articles_list(request):
    template = 'articles/news.html'
    ordering = '-published_at'
    article_ = Article.objects.all().prefetch_related('tags').order_by(ordering)
    content = {'object_list': article_}

    return render(request, template, context=content)


