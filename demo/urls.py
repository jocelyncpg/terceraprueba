from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index, name='index'),
    path('vinilo', views.vinilo, name='vinilo'),
    path('registro', views.registro, name='registro'),
    path('contactanos', views.contactanos, name='contactanos'),
    path('comprar', views.comprar, name='comprar'),  
    path('cassette', views.cassette, name='cassette'),   
    path('cd', views.cd, name='cd'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('loginotros/', views.LoginView.as_view(), name='loginotros'),
    path('logoutotros/', views.LogoutView.as_view(), name='logoutotros'),
    path('pago/', views.PagoView.as_view(), name='pago'),     
    
 
             
    # Ingresar
    path('listadoSQL', views.listadoSQL, name='listadoSQL'),
    path('crud/', views.crud, name='crud'),
    path('alumnosAdd/', views.alumnosAdd, name='alumnosAdd'),
    path('alumnos_del/<str:pk>/', views.alumnos_del, name='alumnos_del'),
    path('alumnos_findEdit/<str:pk>/', views.alumnos_finEdit, name='alumnos_findEdit'),
    path('alumnosUpdate/', views.alumnosUpdate, name='alumnosUpdate'),  
 
]
