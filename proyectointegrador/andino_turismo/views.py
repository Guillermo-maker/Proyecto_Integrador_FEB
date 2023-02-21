from django.shortcuts import render
from django.db.models import Q
from .models import Viaje, Recorrido, Chofer, Bus


def index_view(request):
    return render(request, 'index.html')


def contact(request):
    return render(request, 'contact.html')


def agregarviaje(request):
    return render(request, 'agregarviaje.html')


def login(request):
    return render(request, 'login.html')


def register(request):
    return render(request, 'register.html')


def books(request):
    return render(request, 'books.html')


def listaviaje(request):
    viajes=Viaje.objects.all( )
    queryset = request.GET.get("buscar")
    if queryset:
        viajes = Viaje.objects.filter(
            Q(nombre = queryset) 
        )
        
        
    return render(request, 'listaviaje.html',context={"viaje":viajes}   )


def agregarviaje_view(request):
    bus = Bus.objects.all()
    chofer = Chofer.objects.all()
    recorrido = Recorrido.objects.all()

    return render(request, 'agregarviaje.html', context={"bus": bus, "chofer": chofer, "recorrido": recorrido})


def agregarviaje(request):       
    print(f"---{request.POST}---")

    bus = Bus.objects.filter(numero_unidad=int(request.POST['bus']))
    chofer = Chofer.objects.filter(nombre=str(request.POST['chofer']))
    recorrido = Recorrido.objects.filter(nombre=str(request.POST['recorrido']))

    nombre = request.POST['nombre']
    dia = request.POST['dia']
    hora_inicio_prevista = request.POST['hora_inicio_prevista']
    hora_inicio = request.POST['hora_inicio']
    hora_fin = request.POST['hora_fin']
    numero = request.POST['numero']
    bus = bus[0]
    chofer = chofer[0]
    recorrido = recorrido[0]


    new_viaje = Viaje(nombre=nombre, dia=dia, hora_inicio_prevista =hora_inicio_prevista , hora_inicio=hora_inicio,
                      hora_fin=hora_fin, numero=numero,
                      )
    new_viaje.save()
    return render(request, 'agregarviaje.html')



