from django.shortcuts import render, redirect
from .models import Ingrediente, Pizza, Tamano
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.decorators import login_required, permission_required
from .forms import CustomUserForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User, auth

# Create your views here.
def index(request):
    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate( username=username, password=password)
        login(request, user)

        return redirect('index') 


    return render(request,'appizza/index.html')

def pizzap(request):
    return render(request,'appizza/pizzap.html')

@login_required
def formulario(request):

    tamano = Tamano.objects.all()
    #ing = Ingrediente.objects.all()

    variable = {'tamano':tamano}

    if request.POST:
        pi = Pizza()
        pi.nombre = request.POST.get('txtNombrepizza')
        pi.precio = request.POST.get('txtPrecio')
        #ingr = Ingrediente()
        #ingr.id = request.POST.get('cboi')
        if '' in request.GET:
            pi.ingredientes.add = request.POST.get('cbx1')

        #pi.ingredientes = request.POST.getlist('cbx')
        ta = Tamano()
        ta.id = request.POST.get('cbo')
        pi.tamano = ta

        
        try:
            pi.save()
            variable [ 'mensaje ' ] = 'Guardado'
        except:
            variable [ 'mensaje ' ] = 'no se ha podido guardar :c'


    return render(request,'appizza/formulario.html', variable)

#CRUD 

def listar_pizzas(request):
    pizzas = Pizza.objects.all()
    

    return render(request, 'appizza/listar_pizzas.html', {'pizzas':pizzas} )



def eliminar_pizza(request, id):

    pizza = Pizza.objects.get(id=id)

    try:
        pizza.delete()

        mensaje = "Pizza Eliminada Correctamente"
        messages.success(request, mensaje)
    except:
        mensaje = "no se ha podido eliminar"    
        messages.success(request, mensaje)

    return redirect('listar_pizzas')    



def modificar (request,id):
    pi = Pizza.objects.get(id=id)

    ta = Tamano()
    variable = {'pi':pi, 'ta':ta }

    return render(request, 'appizza/modificar.html', variable)


def registro_usuario(request):
    data = {
        'form':CustomUserForm()
    }

    if request.method == 'POST':

        formu = CustomUserForm(request.POST)

        if formu.is_valid():

            formu.save()
            username = formu.cleaned_data['username']
            password = formu.cleaned_data['password1']
            user = authenticate( username=username, password=password)
            login(request, user)
            return redirect('index')

    return render(request, 'registration/registro.html', data)


def loginn(request):
    return render(request,'registration/login.html')