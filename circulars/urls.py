from django.urls import path
from . import views

urlpatterns = [

    path(
        '',
        views.circular_list,
        name='circular_list'
    ),

]