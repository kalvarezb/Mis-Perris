from django.http import HttpResponse
import requests
from django.shortcuts import render
from  .models import Adoptante

# Create your views here.

def index(request):
    response = requests.get('http://api.ipstack.com/check?access_key=ed45289eb6aa84378442d6c312320945')
    data = response.json()
    correo = request.POST.get('correo', 0)
    rut = request.POST.get('rut',0)
    nombre = request.POST.get('nombre','')
    fechaNac = request.POST.get('fechaNac',0)
    telefono = request.POST.get('telefono',0)
    regio = request.POST.get('regiones',0)
    comunas = request.POST.get('comunas',0)
    tipo = request.POST.get('tipoVivienda',0)
    adoptante = Adoptante(correo = correo, run = rut, nombreCompleto = nombre, pefechaNacimiento = fechaNac,telefono = telefono,region = regio,comuna = comunas,tipoVivienda = tipo)
    adoptante.save()
    return render(request,'index.html',{'latitud': data['latitude'],'longitud': data['longitude'],'ciudad': data['city'],'region': data['region_code'],'ip': data['ip'], 'pais': data['country_name'] })