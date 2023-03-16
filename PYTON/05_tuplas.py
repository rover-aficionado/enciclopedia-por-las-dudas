#tuplas

mi_tupla = tuple()
mi_otra_tupla = ()

#dos formas de definir 

"""una tupla es un conjunto de valores pero no es lo mismo que una lista pero funcionan igual, la diferencia es que son variables constantes o sea no se pueden variar """

mi_tupla = ("roberto", "garcía", 17, 1.75)
mi_otra_tupla = ("hola", "python!")
print(mi_tupla)
print(type(mi_tupla)) 
"""se pueden hacer búsquedas como las listas con mi_tupla[2] empezando desde el 0 como una lista""" 

print(mi_tupla.count("roberto"))
print(mi_tupla.index("roberto")) #posicion de la busqueda 

#mi_tupla[1] = 1.80 no se puede por que las tuplas no se peueden variar 

print(mi_tupla + mi_otra_tupla) 
mi_nueva_tupla = mi_tupla +  mi_otra_tupla 
print(mi_nueva_tupla) 

print(mi_nueva_tupla[3:5]) #se busca entre el elemnto  3 y el 5 sin contar el 5 

"""epuede capmbair de una tupla a una lista y viceversa""" 

mi_tupla = list(mi_tupla)
print(type(mi_tupla))
mi_tupla = tuple(mi_tupla)
print(type(mi_tupla)) 

del mi_tupla #borra la tupla 
print(mi_tupla) #dice que no está definida por que no existe ya