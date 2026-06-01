from django.shortcuts import render, get_object_or_404
from .models import News


def news_list(request):

    news_items = News.objects.order_by(
        '-created_at'
    )

    return render(
        request,
        'news/list.html',
        {
            'news_items': news_items
        }
    )


def news_detail(request, slug):

    article = get_object_or_404(
        News,
        slug=slug
    )

    return render(
        request,
        'news/detail.html',
        {
            'article': article
        }
    )