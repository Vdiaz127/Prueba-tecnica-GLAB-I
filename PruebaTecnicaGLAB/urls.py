"""
URL configuration for PruebaTecnicaGLAB project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from PruebaTecnicaGLAB.views import *
from django.shortcuts import redirect


urlpatterns = [
    path('admin/', admin.site.urls),
    path('iniciar_sesion/',inicio_sesion,name='login'),
    path('registrar_admin/',registrar_administrador, name='registrar admin'),
    path('cerrar_sesion/',cerrar_sesion,name='cerrar sesion'),
    path('reservacion/',registrar_reserva, name='formulario de reservacion'),
    path('lista_reservaciones/',listar_reservaciones,name='lista de reservaciones'),
    path('confirmar_reserva/',confirmar_reserva,name='confirmar reserva'),
    path('editar_datos/',editar_datos,name='editar datos'),
    path('',inicio),
]
