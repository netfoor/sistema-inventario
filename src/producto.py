class Producto:
    """Representa un producto del sistema de inventario."""

    def __init__(self, codigo, nombre, precio, existencia):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.existencia = existencia

    def mostrar_informacion(self)
        print(f"Código: {self.codigo}")
        print(f"Nombre: {self.nombre}")
        print(f"Precio: ${self.precio:.2f}")
        print(f"Existencia: {self.existencia} unidades")
        print("Producto en inventario")


if __name__ == "__main__":
    producto = Producto("P001", "Teclado mecánico", 899.50, 25)
    producto.mostrar_informacion()
