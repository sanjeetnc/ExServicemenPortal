from django.shortcuts import render, get_object_or_404
from .models import WelfareScheme


def welfare_list(request):

    schemes = WelfareScheme.objects.all().order_by('-created_at')

    return render(
        request,
        'welfare/list.html',
        {
            'schemes': schemes
        }
    )


def welfare_detail(request, slug):

    scheme = get_object_or_404(
        WelfareScheme,
        slug=slug
    )

    return render(
        request,
        'welfare/detail.html',
        {
            'scheme': scheme
        }
    )