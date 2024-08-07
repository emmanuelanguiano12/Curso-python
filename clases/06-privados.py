class Perro:
    
    def __init__(self, nombre, edad): #Constructor
        self.__nombre = nombre
        self.edad = edad

    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self, nombre):
        self.__nombre = nombre 

    def habla(self):
        print(f"{self.__nombre} guau")

    @classmethod
    def factory(cls):
        return cls("Chispa", 4) #Hace referencia a Perro


perro1 = Perro.factory()
perro1.habla()
print(perro1.__dict__)