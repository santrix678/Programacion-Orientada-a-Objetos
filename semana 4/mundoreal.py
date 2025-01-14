# Clase Libro
class Libro:
    def __init__(self, titulo, autor, precio):
        self.titulo = titulo
        self.autor = autor
        self.precio = precio

    def mostrar_info(self):
        return f"Título: {self.titulo}, Autor: {self.autor}, Precio: ${self.precio:.2f}"

# Clase Cliente
class Cliente:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
        self.pedidos = []  # Lista de objetos Pedido

    def agregar_pedido(self, pedido):
        self.pedidos.append(pedido)

    def mostrar_pedidos(self):
        if not self.pedidos:
            return f"{self.nombre} no ha realizado ningún pedido."
        resultado = f"Pedidos de {self.nombre}:\n"
        for pedido in self.pedidos:
            resultado += f"- {pedido.mostrar_info()}\n"
        return resultado

# Clase Pedido
class Pedido:
    def __init__(self, cliente, libros):
        self.cliente = cliente
        self.libros = libros  # Lista de objetos Libro

    def mostrar_info(self):
        libros_detalles = ", ".join([libro.titulo for libro in self.libros])
        return f"Pedido para {self.cliente.nombre}: {libros_detalles}"

# Crear objetos de la clase Libro
libro1 = Libro("El Principito", "Antoine de Saint-Exupéry", 10.99)
libro2 = Libro("Cien años de soledad", "Gabriel García Márquez", 15.50)
libro3 = Libro("1984", "George Orwell", 12.75)

# Crear un cliente
cliente1 = Cliente("Ana Pérez", "ana.perez@gmail.com")

# Crear un pedido
pedido1 = Pedido(cliente1, [libro1, libro3])
pedido2 = Pedido(cliente1, [libro2])

# Agregar pedidos al cliente
cliente1.agregar_pedido(pedido1)
cliente1.agregar_pedido(pedido2)

# Mostrar detalles
print(libro1.mostrar_info())
print(cliente1.mostrar_pedidos())
