from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='desp-index'),
     path('Boletaspdf/', views.Boletaspdf, name='desp-Envioboleta'),
     path('salir',views.salir,name='salir'),
]