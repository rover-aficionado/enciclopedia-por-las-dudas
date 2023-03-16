
#modulos

"""cunado se tiene un código en un fichero externo se le puede llamar y usar en este.no funciona si el nombre tiene números"""

import modulos 
modulos.sum_de_valores(4, 6, 8)

"""para imprtar solo una de las funcione que tiene el  fichero se puede llamar solo a la funcion que se quiere ejecuatar
pero si se pone from modulos import (una funcion) solo se llama a una de las funciones que tenga el fichero y el resto no va a funcionar pero poniendo from modulos import (una funcion) ( otra funcion) vas a llammar a varias funciones dentro del otro fichero"""

modulos.sum_de_valores(4, 6, 7)

modulos.print_value("hola mundo!") 

#modulos creados por el sistema

import math  #este vale para hacer operaciones matemáticas que es del sistema, es decir, no lo tengo yo lo tiene python por defecto
import random #hace operaciones aleatorias 

print(math.pi) 
print(math.pow(2, 6)) #son para hacer potencias

from math import pi as pi_value # ahora el valor de pi se llama pi_value, con el as se puede cambiar el nombre.  
print(pi_value) 