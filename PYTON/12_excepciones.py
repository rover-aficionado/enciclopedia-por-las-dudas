#clases

"""valen para eviatr que si existe algun fallo en el código del programa este se pare por completo y continue"""

number_one, number_two = 1, "2"

"""se puede evolucionar con try except else"""
try:  #le digo al programa que pruebe a hacer el print y si falla que haga la parte de except 
    print(number_one + number_two)
except: 
    print("esto ha fallado")

try:  
    print(number_one + number_two)
    print("no se ha producido un error")
except: 
    print("esto ha fallado")
else: 
    print("la ejecuación continua")

#asi va a funcionar bien
number_one, number_two = 1, 2

try:  
    print(number_one + number_two)
    print("no se ha producido un error")
except: 
    print("esto ha fallado")
else: 
    print("la ejecuación continua")


number_one, number_two = 1, "2"

try:  
    print(number_one + number_two)
    print("no se ha producido un error")
except: 
    print("esto ha fallado")
else: 
    print("la ejecuación continua perfectamete")
finally:                            #se va a ejecutar pase lo que pase
    print("la ejecuación continua")

number_one, number_two = 1, 2 

try:  
    print(number_one + number_two)
    print("no se ha producido un error")
except: 
    print("esto ha fallado")
else: 
    print("la ejecuación continua perfecatametne")
finally:
    print("la ejecuacion continua")

# excepción por tipo

try:  
    print(number_one + number_two)
    print("no se ha producido un error")
except TypeError:      #eso solo se va a ejecuatar cuando exista un error de tipo
    print("esto ha fallado")
else: 
    print("la ejecuación continua")  

try:  
    print(number_one + number_two)
    print("no se ha producido un error")
except TypeError: 
    print("exite un type error")
except ValueError: 
    print("existe un value error ")
else: 
    print("la ejecuación continua")

"""va a capturar el error y me va a decir cual es""" 
"""se peude capturar el error"""

number_one, number_two = 1, "2"

try:  
    print(number_one + number_two)
    print("no se ha producido un error")
except TypeError as error: # error es una variable que se crea para la ocasión y que contiene la informacion del error
    print("") 
except Exception as failure: # es un fallo generico
    print(failure)
finally:
    print("hola mundo!")
