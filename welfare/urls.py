from django.urls import path
from . import views

urlpatterns = [

    path(
        '',
        views.welfare_list,
        name='welfare_list'
    ),

    path(
        '<slug:slug>/',
        views.welfare_detail,
        name='welfare_detail'
    ),

]