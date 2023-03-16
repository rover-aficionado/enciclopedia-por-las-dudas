#clases 

class MyEmptyPerson:  #solo en este caso es gramaticalmente correcto   
    pass  

print(MyEmptyPerson) #puede usarse con o sin parentesis 

class MyPerson:
    def __init__(self, name, surname) -> None:    #para definir la clase con esto voy a tener la capacidad de meter parámetros
        self. name = name 
        self.surname = surname       #self se refiere a si mismo, la clase en si misma. he creado dos partes que son name y surname. para que puedan operar en si misma tienen que darse su significado con self.name = name o sea el primer parámetro y self.surname = surname o sea el segundo parámetro que se define en la variable siguiente

my_person = MyPerson("roberto", "garcía")

print(f"{my_person.name} {my_person.surname}")  


class MiPersona:
    def __init__(self, name, surname, alias = "sin alias") -> None: 
        self. full_name = f"{name} {surname} {alias}"  

    def walk (self): 
        print(f"{self.full_name} está caminando") 

mi_person = MiPersona("roberto", "garcia") #se le pasan estos dos parámetros
print(mi_person.full_name) #se usa el nombre de la variable
mi_person.walk()    #se ejecuta la parte de la funcion walk  

mi_person = MiPersona("roberto", "garcia", "rover") #se le pasan estos dos parámetros
print(mi_person.full_name)
mi_person.walk() 