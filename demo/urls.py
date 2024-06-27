from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index, name='index'),
    path('vinilo', views.vinilo, name='vinilo'),
    path('registro', views.registro, name='registro'),
    path('contactanos', views.contactanos, name='contactanos'),
    path('cassette', views.cassette, name='cassette'),   
    path('cd', views.cd, name='cd'),        
    # Ingresar
    path('listadoSQL', views.listadoSQL, name='listadoSQL'),
    path('crud/', views.crud, name='crud'),
    path('alumnosAdd/', views.alumnosAdd, name='alumnosAdd'),
    path('alumnos_del/<str:pk>/', views.alumnos_del, name='alumnos_del'),
    path('alumnos_findEdit/<str:pk>/', views.alumnos_finEdit, name='alumnos_findEdit'),
    path('alumnosUpdate/', views.alumnosUpdate, name='alumnosUpdate'),    
]
