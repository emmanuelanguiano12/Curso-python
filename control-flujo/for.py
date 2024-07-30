buscar = 10

for numero in range(5):
    print(numero)
    if numero == buscar:
        print("encontrado", buscar)
        break
else:
    print(buscar, "No encontrado")

# for char in "Emmanuel":
#     print(char)