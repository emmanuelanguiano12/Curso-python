class Perro:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __del__(self):
        print(f"Adios {self.nombre}")

    def __str__(self):
        return f"Clase perro: {self.nombre}"

    def habla(self):
        print(f"{self.nombre} dice guau")

perro = Perro("coco", 2)
# print(perro)
# texto = str(perro)
# print(texto)

del perro