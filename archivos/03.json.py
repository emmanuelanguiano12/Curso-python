import json
from pathlib import Path

# productos = [
#                 {
#                     "id": 1,
#                     "nombre": "Laptop"
#                 },
#                 {
#                     "id": 2,
#                     "nombre": "Smartphone"
#                 },
#                 {
#                     "id": 3,
#                     "nombre": "Auriculares Bluetooth"
#                 },
#                 {
#                     "id": 4,
#                     "nombre": "Monitor 4K"
#                 },
#                 {
#                     "id": 5,
#                     "nombre": "Teclado Mecánico"
#                 }
#             ]

# data = json.dumps(productos)
# Path("archivos/productos.json").write_text(data)

#Leer json
data = Path("archivos/productos.json").read_text(encoding='utf-8')
productos = json.loads(data)
print(productos)

#Modificar json
productos[0]["nombre"] = "PC Gamer"
Path("archivos/productos.json").write_text(json.dumps(productos))