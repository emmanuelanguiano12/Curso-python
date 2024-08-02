usuarios = [[4, "Emmanuel"], [1, "Carlos"], [5, "Anguiano"]]

# nombres =[]

# for usuario in usuarios:
#     nombres.append(usuario[1])

# print(nombres)

# nombres = [user[1] for user in usuarios]

# filtrar si el id es mayor a 2
# nombres = [user for user in usuarios if user[0] > 2]

# Filtrar y transformar
# nombres = [user[1] for user in usuarios if user[0] > 2]


# nombres = list(map(lambda user: user[1], usuarios))
menosUsers = list(filter(lambda user: user[0] > 2, usuarios))
print(menosUsers)