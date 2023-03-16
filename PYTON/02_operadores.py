"""operadores"""

print(3 + 4)
print(3 - 4)
print(3 / 4)
print(3 * 4)
print(3 % 4) #para saber el resto de una división
print(3 // 4) #la división acabe aproximada a un número entero como sale 0.75 redondea a 0 
print(2**3) 

print("hola" + "hundo!") #une las dos palabras con un menos u otro operador da error

#print("hola" + 5) #da fallo pero se puede cambir a str()
print("hola", str(5)) #da hola 5 
print("hola" * 5) # hola se repite 5 veces 
print("hola" * (2 * 5)) #multiplica 2 * 5 y luego hola * 5 

mi_float = 2.5 * 2 
print("hola" * int(mi_float)) # multiplica la variable, la pasa a número entero y luego lo multiplica por hola

print(3 > 4) #mayor que 
print(3 < 4) #menor que
print(3 <= 4) #menor igual
print(3 >= 4) #mayor igual 
print(3 == 4) #igual 
print(3 != 4) #desigual 

print("hola" > "python")
print("hola" < "python")
print("hola" <= "python") 
print("hola" >= "python")
print("hola" == "python")
print("hola" != "python")
#compara el orden albfabético y  dice si se cumple, es decir, la palabra más cercana al inicio del alfabeto con todas sus letras

#para comparar la cantidad de caracteres se usa el len()
print(len("hola") < len("python"))


#operadores lógicos

print(3  > 4  and "hola" > "python") 
print(3  > 4  or "hola" > "python") 
print(3 < 4 or "hola" > "python" and 4 == 4) #se pueden agrupar las operaciones lógicas y se pueden agruapar con parentesis 

"""print(3  > 4  not  "hola" > "python")  """ # esto está mal porque tiene que negar 
print(not(3 < 4)) #está negando que 3 sea menor que 4 por eso da de resultado False