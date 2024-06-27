from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index, name='index'),
    path('productos', views.productos, name='productos'),
    path('registro', views.registro, name='registro'),
    path('contactanos', views.contactanos, name='contactanos'),    
]
