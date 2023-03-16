#diccionarios 

mi_dic = dict()
mi_otro_dict = {}
print(type(mi_dic)) 

"""se va a agrupar a pares seprados por (:) en los cuales el primero significa el segundo"""

mi_otro_dict = {
    "nombre":"roberto", 
    "apellido":"garcia", 
    "edad":17, 
    1:"python"}  

mi_dic = {
    "nombre":"roberto", 
    "apellido":"garcia", 
    "edad":17, 
    "lenguajes":{"python","html","batch"}
}

print(mi_otro_dict)
print(mi_dic) 
print(len(mi_dic))

print(mi_dic["nombre"]) 

#se puede añadir al diccioanario

mi_dic["calle"] = "calle rover"

del mi_dic["calle"] #para eliminar una parte del diccionario que le he puesto entre []
print(mi_dic)  

print("roberto" in mi_dic) #da false por que se está buscandopor clave, no por valor. si se quiere ver si una palabra está en el diccionario hay que buscar "nombre"
print("nombre"in mi_dic)

print(mi_dic.items()) # indica todo el listado con cada uno de los itemps 
print(mi_dic.keys()) #solo nos da el nombre 
print(mi_dic.values())#solo nos da todos los valores

mi_otro_dict = mi_dic.fromkeys(("nombre","apellido")) #va a craer un diccionario sin valores
print(mi_otro_dict) 


mi_list =["nombre", "piso", 1]
new_dict = dict.fromkeys(mi_list)  
print(new_dict) 

"""el print no es necesario"""
print(list(mi_dic)) #para transforar en una lista 
print(tuple(mi_dic)) #para tranformar en una tupla 
print(set(mi_dic)) #para transgormar en un set 

mi_varaible = mi_otro_dict.values()
print(type(mi_varaible)) #es un diccioanraio de valores se le pueden dar todas las vueltas que se quieran pero va a ser cada vez más rebuscado 

