# numero = 1
# while numero < 100:
#     print(numero)
#     numero +=1

comando = ""
while comando.lower() != "salir":
    comando = input("$ ")
    if comando.lower() != "salir":
        print(comando)