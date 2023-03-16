#condicionales

"""un codicionales es la manera de establaces flujos de ejecuación, es decir, ejecutar las partes del código cuando se den circunstancias especñificas
si se cumple una condición el código se va a ejecuatar usando la lógica boolena"""

mi_condicion = False

if mi_condicion == True: 
    print("se ejecuata la condición de if")

if mi_condicion: 
    print("se ejecuata la condición de if")

#ambas cosas son lo mismo, no es necasario el == True

print("la ejecuación continua")

mi_condicion = 5 * 3

if mi_condicion == 11: 
    print("se ejecuta la condición del segundo if") 

#se está condicionando que mi_condición tenga un valor que en este caso es falso por que 5*2 no es 11. también se pueden usar los simbolos < > == <= >= =! así como las operaciones lógicas de not or and (linea 45)  

if mi_condicion > 10: 
    print("es más que 10")
else: 
    print("es menor o igual a 10")  

if mi_condicion > 10 and mi_condicion < 20:  
    print("es más que 10 y menos que 20")
else: 
    print("es menor o igual a 10")  

if mi_condicion == 11: 
    print("se ejecuta la condición del segundo if") 
elif mi_condicion == 15: 
    print("es igual a 15") 
# elif es para hacer un else if  

mi_str = "hola"

if mi_str: 
    print("mi cadena de texto no está vacía") #lo interpreta como False por que lo interpreta como si no tubiera ni lógica booleana ni valor
else:
    print("mi cadena de textro está vacía")
if not  mi_str: 
    print("mi cadena de texto sigue vacía")  