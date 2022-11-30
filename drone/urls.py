from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('flightdata/', views.flightdata, name='flightdata'),
    path('flightdata-list/<str:reg>/', views.flightdata_list, name='flightdata_list'),
]