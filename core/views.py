from django.shortcuts import render, redirect
from .models import Marca, Automovil
#importamos la mensajeria de django para utilizarla
from django.contrib import messages
# Create your views here.
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'core/home.html')

def galeria(request):
    return render(request, 'core/galeria.html')

def agregar_auto(request):
    #buscaremos todas las marcas
    #y se las enviaremos al template
    marcas = Marca.objects.all()
    variables = {
        'marcas':marcas
    }

    #preguntaremos si la peticion es de tipo POST

    if request.POST:
        #si el request es post obtendremos las variables
        auto = Automovil()
        auto.patente = request.POST.get('txtPatente')
        auto.modelo = request.POST.get('txtModelo')
        auto.anio = request.POST.get('txtAnio')
        #crearemos un objeto Marca para obtener el id de la marca
        marca = Marca()
        marca.id = request.POST.get('cboMarca')
        #guardamos marca dentro de auto
        auto.marca = marca

        #procederemos a guardar al auto en la BBDD
        try:
            auto.save()
            variables['mensaje'] = 'Guardado correctamente'
        except:
            variables['mensaje'] = 'No se ha podido guardar'

    return render(request, 'core/agregar_auto.html', variables)


def listar_autos(request):
    #buscamos todos los automoviles
    autos = Automovil.objects.all()

    variables = {
        'autos':autos
    }

    return render(request, 'core/listar_autos.html', variables)

def eliminar_auto(request, id):
    #primer paso encontrar el automovil
    auto = Automovil.objects.get(id=id)

    #una vez encontrado el automovil se elimina
    try:
        auto.delete()
        messages.success(request, 'Eliminado correctamente')
    except:
        messages.error(request, 'No se ha podido eliminar')
    
    #redirigiremos al usuario de vuelta al listado
    return redirect('listar_autos')
