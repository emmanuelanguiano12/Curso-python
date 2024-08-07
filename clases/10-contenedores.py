class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
    
    def __str__(self):
        return f"Producto: {self.nombre} - Precio: {self.precio}"

class Categoria:
    productos = []

    def __init__(self, nombre, productos):
        self.nombre = nombre
        self.productos = productos

    def agregar(self, producto):
        self.productos.append(producto) #Agregar un producto al listado

    def imprimir(self):
        for producto in self.productos:
            print(producto)

kayak = Producto("Kayak", 1000)
balon = Producto("balon", 300)
bicicleta = Producto("bicicleta", 3000)
deportes = Categoria("Deportes", [kayak, balon])
deportes.agregar(bicicleta)
deportes.imprimir()