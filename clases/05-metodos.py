class Perro:
    patas = 4
    
    def __init__(self, nombre, edad): #Constructor
        self.nombre = nombre
        self.edad = edad

    @classmethod
    def habla(cls):
        print("guau")

    @classmethod
    def factory(cls):
        return cls("Chispa", 4) #Hace referencia a Perro

Perro.habla()
perro1 = Perro("Coco", 2)
perro2 = Perro("Canelo", 3)
perro3 = Perro.factory()
print(perro3.edad, perro3.nombre)