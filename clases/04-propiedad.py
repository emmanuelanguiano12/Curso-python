class Perro:
    patas = 4
    
    def __init__(self, nombre, edad): #Constructor
        self.nombre = nombre
        self.edad = edad

    def habla(self):
        print(f"{self.nombre} dice: guau y tiene {self.edad} años")

Perro.patas = 2
miPerro = Perro("Coco", 19)
miPerro.patas = 5
miPerro2 = Perro("Canelo", 19)
print(Perro.patas)
print(miPerro.patas)