#listas 

mi_lista = list() 
mi_otra_lista = [] 
"""se pueden hacer de las dos maneras"""

"""una lista es una forma de agrupar datos"""
print(len(mi_lista)) #da 0 por que no tiene nada 

mi_lista = [35, 24, 62, 52, 30, 17]
print(mi_lista)
print(len(mi_lista))

mi_otra_lista = [17, 1.75, "roberto", "garcía"]
print(type(mi_otra_lista)) # va a definir lo que es, en este caso es una lista 

print (mi_otra_lista[0]) #el primer elemento es el 0 no el 1 por eso se pone 0 
print(mi_otra_lista[-1])
"""si sepone números negativos va a empezar desde el final"""
print(mi_otra_lista[1])
print(mi_otra_lista[3])
print(mi_otra_lista[-4])
"""va a ir colocando laa posición, si es negativa va a epezar desde el final. siempre empezando desde 0 siempre y cuando pongas el nímero correcto, si es más da error """

print(mi_otra_lista.count("roberto"))  #count() retormna el número de veces que aparece un valor

age, height, name, surname = mi_otra_lista
print (name) 

mi_otra_lista = mi_otra_lista[1], mi_otra_lista[2] #es una forma rebuscada de ordenar una lista
mi_otra_lista = [17, 1.75, "roberto", "garcía"]

print(mi_lista + mi_otra_lista)   

mi_lista = "hola python!" 
print(mi_lista)  

#para añadir algun elemento 
mi_otra_lista.append("hola mundo!") #para añadir a la lista otro valor 
print(mi_otra_lista)
mi_otra_lista.insert(1, "azul")# va a añadir en la posición 1 otro valor 
print(mi_otra_lista)

mi_otra_lista.remove("azul") #le voy a quiatr un valor, si está repetido solo elimina uno 
print(mi_otra_lista)

print(mi_otra_lista.pop(2)) #va a quitar el elemto que yo le he eindicado 

mi_pop_element = mi_otra_lista.pop(2)
print(mi_pop_element)

del mi_otra_lista[2] #para borrar un elemento
print(mi_otra_lista)

"""la diferencia entre el del y el remove es que en el remove yo se sabe lo que se quiere borrar y el del eleimina por indice o sea la posición que se indica """

print(mi_otra_lista)
mi_otra_lista[1] = "rojo" # va a sustituir la posición que yo le he dado por otro elemento 
print(mi_otra_lista)

mi_nueva_lista = mi_otra_lista.copy() #se ha copaido la variable y a  partir de ahora puedo hacer lo que quiera con ella que se amtiene su estado original

mi_otra_nueva_lista = [1, 8, 5, 78, 95]
mi_otra_nueva_lista.sort
print(mi_otra_nueva_lista) #ordena de menor a mayor los números o en orden alfabético 