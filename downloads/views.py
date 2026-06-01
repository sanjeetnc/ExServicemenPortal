from django.shortcuts import render
from .models import Download


def download_list(request):

    category = request.GET.get('category')

    downloads = Download.objects.all()

    if category:
        downloads = downloads.filter(
            category=category
        )

    return render(
        request,
        'downloads/list.html',
        {
            'downloads': downloads,
            'selected_category': category
        }
    )