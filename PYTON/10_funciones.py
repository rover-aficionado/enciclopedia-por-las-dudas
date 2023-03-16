#funciones 
"""valen para encapsular una lógica concreta y para evitar errores""" 

def mi_funcion (): 
    print("esto es una función") 

mi_funcion ()

def sum_two_values(first_number, second_number): #dentro de los parentesis están los parámentros que se tienen que añadir
    print(first_number + second_number) 

sum_two_values (3, 5)  
sum_two_values (7.9, 4)

# al ser de tipado debil se puede meter un str y va a concatenerse como tal pero no va con str e int en el mismo parámetro

def sum_two_values_with_retur(first_number, second_number): 
    return first_number + second_number 

my_result2 = sum_two_values_with_retur (10, 9) 
my_result = sum_two_values(7.9, 4)
print(my_result) #da none por que no retorna nada (sum_two_values)
print(my_result2) #al rener el retrun si va a devolver el resultado 

def print_name(name, surname):
    print(f"{name} {surname}")

print_name("roberto", "garcía") 
print_name(surname = "roberto", name = "garcía") #se puede indicar cual es cual 

def print_name_with_default(name, surname, alias = "sin alias"): #se le puede llamar a un valor por defecto (alias = "sin alias")
    print(f"{name} {surname} {alias}")   

print_name_with_default("roberto", "garcia", "rover") 
print_name_with_default("roberto", "garcia") 

def print_texts(*text): #con un parametro y delante * se le pueden pasar los parámetros que quiera 
    print(text)

print_texts("hola", "python", "mundo!") 

def print_texts(*text): #se imprimen en varias lineas de elementos infinitos
    for text in text: 
        print(text)

print_texts("hola", "python", "mundo!")  

def upper_txt (*txt): 
    for txt in txt: 
        print(txt.upper())

upper_txt("hola")

    