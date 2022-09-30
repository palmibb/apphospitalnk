"""househo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from apphospitalbk import views

urlpatterns = [
    path('login/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path('user/', views.userView.UsuarioListView.as_view()),
    path('user/<int:pk>/', views.userView.UsuarioRetrieveUpdateDestroy.as_view()),
    path('medico/', views.medicoView.MedicoListCreateView.as_view()),
    path('medico/<int:pk>/', views.medicoView.MedicoRetrieveUpdate.as_view()),
    path('paciente/', views.pacienteView.PacienteListCreateView.as_view()),
    path('paciente/<int:pk>/', views.pacienteView.PacienteRetrieveUpdate.as_view()),
    path('auxiliar/', views.auxiliarView.AuxiliarListCreateView.as_view()),
    path('auxiliar/<int:pk>/', views.auxiliarView.AuxiliarRetrieveUpdate.as_view()),
] 