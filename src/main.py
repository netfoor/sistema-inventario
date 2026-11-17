"""Menú de consola del Sistema de Inventario."""

from producto import Producto


def registrar_producto(inventario, codigo, nombre, precio, existencia):
    """Agrega un producto al inventario. El código no se puede repetir."""
    if any(p.codigo == codigo for p in inventario):
        raise ValueError(f"Ya existe un producto con el código {codigo}")
    producto = Producto(codigo, nombre, float(precio), int(existencia))
    inventario.append(producto)
    return producto


def buscar_producto(inventario, codigo):
    """Devuelve el producto con ese código, o None si no existe."""
    return next((p for p in inventario if p.codigo == codigo), None)


def consultar_productos(inventario):
    """Muestra todos los productos registrados."""
    if not inventario:
        print("No hay productos registrados.")
        return
    for producto in inventario:
        producto.mostrar_informacion()
        print()


def menu(entrada=input):
    inventario = []
    while True:
        print("\nSISTEMA DE INVENTARIO")
        print("1. Registrar producto")
        print("2. Consultar productos")
        print("3. Buscar producto por código")
        print("0. Salir")
        opcion = entrada("Opción: ").strip()
        if opcion == "1":
            try:
                producto = registrar_producto(
                    inventario,
                    entrada("Código: ").strip(),
                    entrada("Nombre: ").strip(),
                    entrada("Precio: "),
                    entrada("Existencia: "),
                )
                print(f"Producto {producto.codigo} registrado.")
            except ValueError as error:
                print(f"No se registró el producto: {error}")
        elif opcion == "2":
            consultar_productos(inventario)
        elif opcion == "3":
            producto = buscar_producto(inventario, entrada("Código: ").strip())
            if producto:
                producto.mostrar_informacion()
            else:
                print("No se encontró el producto.")
        elif opcion == "0":
            print("Hasta luego.")
            return inventario
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    menu()
