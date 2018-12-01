from django.http import HttpResponse
import requests
from django.shortcuts import render
from  .models import Adoptante

# Create your views here.

def index(request):
    response = requests.get('http://api.ipstack.com/check?access_key=ed45289eb6aa84378442d6c312320945')
    data = response.json()
    return render(request,'index.html',{'latitud': data['latitude'],'longitud': data['longitude'],'ciudad': data['city'],'region': data['region_code'],'ip': data['ip'], 'pais': data['country_name'] })

def formulario(request):
    correo = request.POST.get('email', 0)
    rut = request.POST.get('rut',0)
    nombres = request.POST.get('nombres','')
    fechaNacimiento = request.POST.get('fecha_nacimiento',0)
    telefono = request.POST.get('telefono',0)
    region = request.POST.get('region',0)
    ciudad = request.POST.get('ciudad',0)
    tipoVivienda = request.POST.get('tipo_vivienda',0)
    adoptante = Adoptante(correo = correo, rut = rut, nombres = nombres, pefechaNacimiento = fechaNacimiento, telefono = telefono, region = region, ciudad = ciudad,tipoVivienda = tipoVivienda)
    adoptante.save()
    return render(request, 'formulario.html', {})