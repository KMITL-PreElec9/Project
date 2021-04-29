from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'), 
    path('showdata', views.show_data, name='showdata'),
    path('testweb', views.test_camp, name='testweb'),
]