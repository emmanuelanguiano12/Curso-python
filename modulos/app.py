import usuarios.acciones
from usuarios.acciones.usuario import guardar, pagar_impuestos

guardar()
pagar_impuestos()
print(dir(usuarios.acciones))