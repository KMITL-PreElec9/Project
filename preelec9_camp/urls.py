from django.urls import path

from . import views

urlpatterns = [
    path('preelec9-camp', views.index)
]