class Model:
    tabla = False

    def __init__(self):
        if not self.tabla:
            print("Error, tienes que definir una tabla")
    
    def guardar(self):
        print(f"Guardando {self.tabla} en BD")

    @classmethod
    def buscarPorId(self, _id):
        print(f"Buscando por id: {_id} en la tabla: {self.tabla}")

class Usuario(Model):
    tabla = "Usuario"

usuario = Usuario()
usuario.guardar()
Usuario.buscarPorId(2)