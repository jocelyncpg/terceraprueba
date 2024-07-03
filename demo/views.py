from django.shortcuts import render
from .models import Album, Musician, Postulante, Genero 
from .forms import AlbumForm
from django.contrib.auth.decorators import login_required

    
# Create your views here.
def index(request):
    context={"clase": "inicio"}
    return render(request, 'demo/index.html', context)

def vinilo(request):
    context={"clase": "vinilo"}
    return render(request, 'demo/vinilo.html', context)


def registro(request):
    context={"clase": "registro"}
    return render(request, 'demo/registro.html', context)



@login_required
def login(request):
    context={}
    return render(request, 'accounts/login.html', context)

def contactanos(request):
    context={}
    return render(request, 'demo/contactanos.html', context)

def cassette(request):
    context={}
    return render(request, 'demo/cassette.html', context)

def cd(request):
    context={}
    return render(request, 'demo/cd.html', context)

def comprar(request):
    context={}
    return render(request, 'demo/comprar.html', context)

# ingresar

def listadoSQL(request):
    # demo=Album.objects.raw('SELECT * FROM demo_Album')
    demo = Postulante.objects.all()
    print(demo)
    context={"demo": demo}
    return render(request, 'demo/listadoSQL.html', context)

def crud(request):
    demo = Postulante.objects.all()
    context={"demo": demo}
    return render(request, 'demo/alumnos_list.html', context)


def alumnosAdd(request):
    if request.method != "POST":
        generos = Genero.objects.all()
        context = {"generos": generos}
        return render(request, 'demo/alumnos_add.html', context)
    else:
        rut = request.POST["rut"]
        nombre = request.POST["nombre"]
        aPaterno = request.POST["paterno"]
        aMaterno = request.POST["materno"]
        fechaNac = request.POST["fechaNac"]
        genero = request.POST["genero"]
        telefono = request.POST["telefono"]
        email = request.POST["email"]
        direccion = request.POST["direccion"]
        activo = "1"

        objGenero = Genero.objects.get(id_genero=genero)
        obj = Postulante.objects.create(
            rut=rut,
            nombre=nombre,
            apellido_paterno=aPaterno,
            apellido_materno=aMaterno,
            fecha_nacimiento=fechaNac,
            id_genero=objGenero,  # Asociar el genero correctamente
            telefono=telefono,
            email=email,
            direccion=direccion,
            activo=activo
        )
        obj.save()
        context = {'mensaje': "OK, datos grabados..."}
        return render(request, 'demo/alumnos_add.html', context)
    
def alumnos_del(request, pk):
    context={}
    try:
        postulante = Postulante.objects.get(rut=pk)
        postulante.delete()
        mensaje ="Bien, datos eliminados..."
        postulantes = Postulante.objects.all()
        context = {'postulantes': postulantes, 'mensaje': mensaje}
        return render(request, 'demo/alumnos_list.html', context)
    except:
        mensaje = "Error, rut no existe..."
        alumnos = Postulante.objects.all()
        context = {'postulantes': postulante, 'mensaje': mensaje}
        return render(request, 'demo/alumnos_list.html', context)
        
def alumnos_finEdit(request,pk):
    if  pk != "":
        postulante = Postulante.objects.get(rut=pk)
        generos = Genero.objects.all()
            
        print(type(postulante.id_genero.genero))
            
        context={'postulante':postulante, 'generos': generos}
    if postulante:
        return render(request, 'demo/alumnos_edit.html', context)
    else:
        context={'mensaje':"Error, rut no existe..."}
        return render(request, 'demo/alumnos_list.html', context)
            
def alumnosUpdate(request):
    if request.method == "POST":
        rut = request.POST["rut"]
        nombre = request.POST["nombre"]
        apaterno = request.POST["paterno"]
        amaterno = request.POST["materno"]
        fechaNac = request.POST["fechaNac"]
        genero = request.POST["genero"]
        telefono = request.POST["telefono"]
        email = request.POST["email"]
        direccion = request.POST["direccion"]
        activo = "1"

        objGenero = Genero.objects.get(id_genero=genero)
        postulante = Postulante()
        postulante.rut = rut
        postulante.nombre = nombre
        postulante.apellido_paterno = apaterno
        postulante.apellido_materno = amaterno
        postulante.fecha_nacimiento = fechaNac
        postulante.id_genero = objGenero  # Asociar el genero correctamente
        postulante.telefono = telefono
        postulante.email = email
        postulante.direccion = direccion
        postulante.activo = activo
        postulante.save()

        generos = Genero.objects.all()
        context = {
            'mensaje': "Datos actualizados",
            'generos': generos,
            'postulante': postulante
        }
        return render(request, 'demo/alumnos_edit.html', context)
    else:
        postulantes = Postulante.objects.all()
        context = {'postulantes': postulantes}
        return render(request, 'demo/alumnos_list.html', context)
    
    
   