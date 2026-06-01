from django.shortcuts import render
from .models import TrustActivity


def trust_list(request):

    activities = TrustActivity.objects.order_by(
        '-event_date'
    )

    return render(
        request,
        'trust/list.html',
        {
            'activities': activities
        }
    )