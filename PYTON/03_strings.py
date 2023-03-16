#strings o str 

mi_string = "mi str"
mi_otro_string = "mi otro str"

print(len(mi_string))
print(len(mi_otro_string))

print(mi_string + mi_otro_string)
print(mi_string + " " + mi_otro_string) 

mi_nueva_linea_str = "este es un str\ncon salto de línea"
print(mi_nueva_linea_str)

mi_tab_str = "eso tes un str\tcon tabulación"
print(mi_tab_str)

mi_escape_str = "\t esto es un str \n escapado "
print(mi_escape_str)

mi_escape_str = "\\t esto es un str \n escapado "
print(mi_escape_str) #con una doble barra se puede cancelar la función dada por el \n o \t 

"""formateo"""

name, surname, age = "benito", "camela", 35 

print("mi nombre es {} {} y mi edad es {}". format(name, surname, age ))
print("mi nombre es %s %s y mi edad es %d" %(name, surname, age))

"""en el primero es necesario indocar donde va cada variable con {} pero solo cuando se llama a format() si no al poner los %s fura del str se va a poner %(). el %d es una forma de indicar que solo se puede idar un número"""

print(f"mi nombre es {name} {surname} y mi edad es {age}") #la f sirve para formatear y dar las variables

"""desempaquetado de caracteres"""
lengua = "python"
a, b, c, d, e, f  = lengua

print(a)
print(b)
print(c)
print(d)
print(e)
print(f) 

"""división"""

lengua_slice = lengua[1:3]
print(lengua_slice)

lengua_slice = lengua[1:]
print(lengua_slice)

lengua_slice = lengua[-2]
print(lengua_slice)

lengua_slice = lengua[0:6:2] #va a saltar uno de los caracteres
print(lengua_slice)

"""dar la vuelta"""

lengua_invertida = lengua[::-1] #para dar la vuelta a la palabra se usa ::-1 entre [] algo así  [::-1]
print(lengua_invertida) 

print (lengua.capitalize()) #va a poner letras en mayúscula, en este caso la primera  
print (lengua.upper()) #todo mayusculas 
print (lengua.count("t")) #cuanta la cantidad de letras indicadas en este caso la t 
print (lengua.isnumeric()) #dice si es o no un número 
print ("1".isnumeric())
print (lengua.lower()) 
print ("PYTHON".lower()) #va a devolver todas minúsculas 
print (lengua.upper().isupper()) #va a pasar todas a mayuscula y con isupper() va a indicar si son mayusculas
print (lengua.startswith("py")) #va a comprobar si la variable lengua empieza o no por py 