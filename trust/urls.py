from django.urls import path
from . import views

urlpatterns = [

    path(
        '',
        views.trust_list,
        name='trust_list'
    ),

]