from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('addflight/', views.addflight, name='addflight'),
    path('rpasflights/<str:reg>/', views.rpasflights, name='rpasflights'),
]