class Animal:
    def comer(self):
        print("Comiendo")

class Perro(Animal): #Heredar la clase Animal
    def pasear(self):
        print("Paseando")

class Coco(Perro): #Hererar Perro que ya hereda Animal
    def programar(self):
        print("Programando")

coco = Coco()
perro = Perro()