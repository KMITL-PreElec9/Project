from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('register/<int:page_id>', views.register),
    path('register/', views.register)
]