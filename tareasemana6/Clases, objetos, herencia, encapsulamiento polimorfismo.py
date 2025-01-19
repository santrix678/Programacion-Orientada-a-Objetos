# Clase base: Vehiculo
class Vehiculo:
    def __init__(self, marca, modelo, año):
        # Encapsulación: atributo protegido
        self._marca = marca
        self._modelo = modelo
        self._año = año

    def mostrar_info(self):
        """Método para mostrar la información básica del vehículo."""
        return f"Marca: {self._marca}, Modelo: {self._modelo}, Año: {self._año}"

    def encender(self):
        """Ejemplo de polimorfismo: Método que será sobrescrito en la clase derivada."""
        return "El vehículo está encendido."


# Clase derivada: Automovil (Hereda de Vehiculo)
class Automovil(Vehiculo):
    def __init__(self, marca, modelo, año, puertas):
        super().__init__(marca, modelo, año)
        self.puertas = puertas  # Atributo adicional específico de Automóvil

    def mostrar_info(self):
        """Sobrescritura del método mostrar_info (Polimorfismo)."""
        return f"Automóvil - Marca: {self._marca}, Modelo: {self._modelo}, Año: {self._año}, Puertas: {self.puertas}"

    def encender(self):
        """Sobrescritura del método encender."""
        return "El automóvil está encendido."


# Clase derivada: Motocicleta (Hereda de Vehiculo)
class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, año, tipo):
        super().__init__(marca, modelo, año)
        self.tipo = tipo  # Atributo adicional específico de Motocicleta

    def mostrar_info(self):
        """Sobrescritura del método mostrar_info (Polimorfismo)."""
        return f"Motocicleta - Marca: {self._marca}, Modelo: {self._modelo}, Año: {self._año}, Tipo: {self.tipo}"

    def encender(self):
        """Sobrescritura del método encender."""
        return "La motocicleta está encendida."


# Función principal para demostrar la funcionalidad del programa
if __name__ == "__main__":
    # Instancia de Automóvil
    automovil = Automovil("Toyota", "Corolla", 2020, 4)
    print(automovil.mostrar_info())  # Demostración de herencia y polimorfismo
    print(automovil.encender())

    # Instancia de Motocicleta
    motocicleta = Motocicleta("Yamaha", "MT-07", 2021, "Deportiva")
    print(motocicleta.mostrar_info())  # Demostración de herencia y polimorfismo
    print(motocicleta.encender())
