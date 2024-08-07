class Perro:
    def __init__(self, nombre, edad): #Constructor
        self.nombre = nombre
        self.edad = edad

    def habla(self):
        print(f"{self.nombre} dice: guau y tiene {self.edad} años")

miPerro = Perro("Coco", 19)
miPerro.habla()