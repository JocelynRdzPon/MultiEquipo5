"""
URL configuration for webproject project.

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
from webapp.views import index
from hospitales.views import detalleConsulta, detallePaciente, detalleDoctor, detalleExpediente, detalleHospital, detalleHabitacion, nuevoPaciente,nuevaConsulta, nuevoDoctor, nuevoExpediente, nuevoHospital, nuevaHabitacion, editarPaciente, editarConsulta, editarDoctor, editarExpediente, editarHospital, editarHabitacion, eliminarPaciente, eliminarConsulta, eliminarDoctor, eliminarExpediente, eliminarHospital, eliminarHabitacion

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name='index'),
    
    path('detalle_paciente/<int:id>', detallePaciente),
    path('nuevo_paciente', nuevoPaciente),
    path('editar_paciente/<int:id>', editarPaciente),
    path('eliminar_paciente/<int:id>',eliminarPaciente),

    path('detalle_consulta/<int:id>', detalleConsulta),
    path('nueva_consulta', nuevaConsulta), 
    path('editar_consulta/<int:id>', editarConsulta),
    path('eliminar_consulta/<int:id>', eliminarConsulta),

    path('detalle_doctor/<int:id>', detalleDoctor),
    path('nuevo_doctor', nuevoDoctor),
    path('editar_doctor/<int:id>', editarDoctor),
    path('eliminar_doctor/<int:id>',eliminarDoctor),

    path('detalle_expediente/<int:id>', detalleExpediente),
    path('nuevo_expediente', nuevoExpediente),
    path('editar_expediente/<int:id>', editarExpediente),
    path('eliminar_expediente/<int:id>',eliminarExpediente),

    path('detalle_hospital/<int:id>', detalleHospital),
    path('nuevo_hospital', nuevoHospital),
    path('editar_hospital/<int:id>', editarHospital),
    path('eliminar_hospital/<int:id>',eliminarHospital)
]

