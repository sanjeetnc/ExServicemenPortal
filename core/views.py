from django.shortcuts import render
from welfare.models import WelfareScheme
from downloads.models import Download
from circulars.models import Circular
from news.models import News
from trust.models import TrustActivity


def home(request):

    latest_downloads = Download.objects.order_by('-created_at')[:4]

    latest_circulars = Circular.objects.order_by('-publish_date')[:5]

    latest_news = News.objects.order_by('-created_at')[:3]

    featured_activities = TrustActivity.objects.filter(
        is_featured=True
    )[:3]

    context = {

        'latest_downloads': latest_downloads,
        'latest_circulars': latest_circulars,
        'latest_news': latest_news,
        'featured_activities': featured_activities,

    }

    return render(
        request,
        'core/home.html',
        context
    )