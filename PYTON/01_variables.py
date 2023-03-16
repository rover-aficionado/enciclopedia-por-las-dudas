#variables 

"""por acuerdos se ponen todas las letras en minúscula y entre las palabras una barra baja"""

mi_str_variable = "hola mundo!"
mi_int_variable = 4 
#mi_bool_variable = false
mi_int_to_str_variable = str(mi_int_variable)

print(mi_str_variable, mi_int_variable)  
print(type(mi_int_to_str_variable))

print(type(print("mi cadena de texto"))) # es NoneType por que eal ser una función no es ningún tipo de dato

"""algunas funcione del sistema"""
print(len(mi_int_to_str_variable)) #cuneta los  caracteres contando los espacios
print("este es el valor de:", mi_int_variable) 
"""variables en una sola línea"""

#se puede hacer pero no es la mejor práctica
name, surname, alias, edad  = "roberto", "garcía", "rover", 18 
print(name, surname, alias)
print(surname, alias, name)
print(alias, name, surname) 
print("hola!, mi nombre es", name,"mi apellido es", surname, "pero me llaman", alias, "tengo", edad)  

#para añadir datos se usa input() las variables se pueden sobrescribir para que cambien 
"""
first_name = input ("cual es tu nombre: ")
age = input("que edad tienes: ")

print(first_name)
print(age)
""" 

#forzamos el tipo
address: str = "mi dirección" 
address = 32 
print(address) 
#en los imput() tiene mas sentido pero en este caso es un tipado debil