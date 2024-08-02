mascotas = ["Perro", "Gato", "Ballena", "Leon","Gato", "Tortuga", "Felino"]

mascotas.insert(1, "Pescado")
mascotas.append("Vaca")

#Va el elemento que se quiere eliminar y si está repetido solo elmina el primero
mascotas.remove("Gato") 

mascotas.pop(1)
del mascotas[0]
mascotas.clear()

print(mascotas)