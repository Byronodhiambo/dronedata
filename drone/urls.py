from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('addflight/', views.addflight, name='addflight'),
    path('flights/<str:reg>/', views.flights, name='rpasflights'),
    path('rpas/', views.rpas, name='rpasflights'),
]