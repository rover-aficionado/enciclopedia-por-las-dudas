# sets 

"""es una forma de poner datos, es una forma poco común"""
mi_set = set()
mi_otro_set = {} #inicailemte es un diccionario pero al darle valores se pone como set 
 
print(type(mi_set))

mi_otro_set = {"roberto", "garcía", 1.75, 17} 

print(len(mi_otro_set)) #tiene 4 elementos

print(mi_otro_set) 

mi_otro_set.add("rover")
print(mi_otro_set)
"""un set no es una estructura ordenada"""
mi_otro_set.add("rover")
print(mi_otro_set) 

"""un set no admite repetidos """

print("rover" in mi_otro_set) #true por que rover está dentro 
print("rober" in mi_otro_set) #false por que rober no está dentro

"""para verificar si una palabra estña dentro de un set"""

mi_otro_set.remove("rover") #se pueden eliminar 
print(mi_otro_set)

mi_otro_set.clear() #elimina el interior del set 
print(len(mi_otro_set)) 

del mi_otro_set #elimina el set 
#print(mi_otro_set) 

mi_set = {"roberto", "garcia", 17}
mi_lista = list(mi_set)
print(mi_lista)  

mi_set = {"roberto", "garcía", 1.75, 17} 
mi_otro_set = {"python", "html", "batch"}

mi_nuevo_set = mi_otro_set.union(mi_set) 
print(mi_nuevo_set)

print(mi_nuevo_set.difference(mi_set)) # nos dice la diferencia, es decir nos dice mi_nuevo_set sin tener los elementos de mi_set que añadí en el anterior  