#bucles, loops y ciclos
"""son lo mismo pero con tres nombres"""

"""es un mecanismo que vale para iterar o repetir algo, o sea, pasa por el mismo código varias veces""" 

mi_condicion = 0
while mi_condicion < 10:  #mientras mi_condición sea menor que 10 que haga lo de abajo
    print(mi_condicion)
    mi_condicion += 1 #vale para que se incremente uno cada vez
if mi_condicion == 10: 
  print("mi condición es igual a 10")  

# no puede funcionar el elif 

while mi_condicion < 20 :
    print("mi condición es menor que 20")
    mi_condicion += 3
    if mi_condicion == 15:
        print("mi condición es igual a 15 y se detiene la ejecuación")
        break #para detener la ejecución 
print("mi condición es igual a 20") 

"""for 
par el for se va a tener que usar una lista, tupla, set o diccionario"""

mi_lista = [35, 58, 98, 57, 89, 36, 82]

for element in mi_lista: #el for se va a ejecuar tantas veces como elemtos tenga la lista
    print(element) 

mi_tupla = (35, 58, 98, 57, 89, 36, 82)

for element in mi_tupla: #el for se va a ejecuar tantas veces como elemtos tenga la lista
    print(element) 

mi_set = {35, 58, 98, 57, 89, 36, 82}

for element in mi_set: #el for se va a ejecuar tantas veces como elemtos tenga la lista
    print(element) 

mi_dict = {35:58, 98:57, 89:36, 82:15}

for element in mi_dict: #el for se va a ejecuar tantas veces como elemtos tenga la lista
    print(element) 

"""se pede parar el bucle con break siempre en un if y para continuar se usa el continue pero continua desde el principio del bucel y deteniendo la ejecución en ese punto"""

