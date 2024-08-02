punto = {"x": 25, "y": 50}
print(punto)
print(punto["x"])
print(punto["y"])

punto["z"] = 100
# print(punto, punto["c"])
if "c" in punto:
    print(punto["c"])

print(punto.get("x"))
print(punto.get("c", 75))
del punto["x"]
del (punto["y"])

print(punto)
punto["x"] = 25

for valor in punto:
    print(valor, punto[valor])

for valor in punto.items():
    print(valor)

for llave, valor in punto.items():
    print(llave, valor)

usuarios = [
    {"id": 1, "nombre": "Emmanuel"},
    {"id": 2, "nombre": "Carlos"},
    {"id": 3, "nombre": "Anguiano"},
    {"id": 4, "nombre": "Pedraza"},
]

for user in usuarios:
    print(user["nombre"])