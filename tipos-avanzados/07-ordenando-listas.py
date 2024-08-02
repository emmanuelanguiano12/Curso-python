numeros = [5, 63, 6, 23, 22, 90, 45]

# numeros.sort(reverse=True)
listaArreglada = sorted(numeros, reverse=True)

print(numeros)
print(listaArreglada)

usuarios = [[4, "Emmanuel"], [1, "Carlos"], [5, "Anguiano"]]

usuarios.sort(key=lambda el: el[1]) #lambda para funcniones anonimas o funciones que solo se utilizan una sola vez
print(usuarios)