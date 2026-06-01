from django.shortcuts import render
from .models import Circular


def circular_list(request):

    circulars = Circular.objects.order_by(
        '-publish_date'
    )

    return render(
        request,
        'circulars/list.html',
        {
            'circulars': circulars
        }
    )