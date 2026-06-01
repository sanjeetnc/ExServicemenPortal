from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns



urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
    
    path('admin/', admin.site.urls),

    path('', include('core.urls')),
    
    path('contact/', include('contact.urls')),
    
    path('about/', include('about.urls')),
    
    path(
    'welfare/',
    include('welfare.urls')
),
    
    path(
    'downloads/',
    include('downloads.urls')
),
    
    path(
    'circulars/',
    include('circulars.urls')
),
    
    path(
    'news/',
    include('news.urls')
),
    
    path(
    'trust/',
    include('trust.urls')
),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )