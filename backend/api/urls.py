from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.getAlgoritmos), 
    path('create', views.createAlgoritmo), 
    path('update/<int:id>', views.updateAlgoritmo), 
    path('delete/<int:id>', views.deleteAlgoritmo),
    path('ejecutar_algoritmo/<int:id>', views.ejecutarAlgoritmo),
]
