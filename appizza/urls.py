from django.urls import path
from .views import index, pizzap, formulario, listar_pizzas, eliminar_pizza, modificar,registro_usuario



urlpatterns = [
    path('', index, name="index"),
    path('pizzap/', pizzap, name="pizzap"), 
    path('formulario/', formulario, name="formulario"), 
    path('listar-pizzas/', listar_pizzas, name="listar_pizzas"), 
    path('eliminar-pizza/<id>/', eliminar_pizza, name="eliminar_pizza"),
    path('eliminar-pizza/<id>/', eliminar_pizza, name="eliminar_pizza"),
    path('modificar-pizza/<id>/', modificar, name="modificar"),
    path('registro/', registro_usuario, name="registro_usuario")
]
