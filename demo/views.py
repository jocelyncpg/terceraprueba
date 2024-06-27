from django.shortcuts import render

# Create your views here.
def index(request):
    context={"clase": "inicio"}
    return render(request, 'demo/index.html', context)

def productos(request):
    context={"clase": "productos"}
    return render(request, 'demo/productos.html', context)

def registro(request):
    context={"clase": "registro"}
    return render(request, 'demo/registro.html', context)

def login(request):
    context={}
    return render(request, 'accounts/login.html', context)

def contactanos(request):
    context={}
    return render(request, 'demo/contactanos.html', context)