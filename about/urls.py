from django.urls import path
from . import views

urlpatterns = [

    path('', views.about_page, name='about'),

    path(
        'privacy-policy/',
        views.privacy_policy,
        name='privacy_policy'
    ),

    path(
        'terms/',
        views.terms_conditions,
        name='terms_conditions'
    ),

    path(
        'disclaimer/',
        views.disclaimer,
        name='disclaimer'
    ),

]