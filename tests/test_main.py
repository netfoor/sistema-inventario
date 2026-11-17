"""Pruebas del menú de registro y consulta (v1.1.0)."""

import pytest

from main import buscar_producto, consultar_productos, menu, registrar_producto


def test_cp08_registrar_producto():
    """CP08 - Registrar producto"""
    inventario = []
    producto = registrar_producto(inventario, "P001", "Teclado", "350", "10")
    assert inventario == [producto]
    assert (producto.precio, producto.existencia) == (350.0, 10)


def test_cp09_rechazar_codigo_repetido():
    """CP09 - Rechazar código repetido"""
    inventario = []
    registrar_producto(inventario, "P001", "Teclado", 350, 10)
    with pytest.raises(ValueError):
        registrar_producto(inventario, "P001", "Mouse", 180, 5)
    assert len(inventario) == 1


def test_cp10_consultar_productos(capsys):
    """CP10 - Consultar productos"""
    inventario = []
    registrar_producto(inventario, "P001", "Teclado", 350, 10)
    registrar_producto(inventario, "P002", "Mouse", 180, 5)
    consultar_productos(inventario)
    salida = capsys.readouterr().out
    assert "Nombre: Teclado" in salida and "Nombre: Mouse" in salida


def test_cp11_buscar_producto():
    """CP11 - Buscar producto"""
    inventario = []
    registrar_producto(inventario, "P002", "Mouse", 180, 5)
    assert buscar_producto(inventario, "P002").nombre == "Mouse"
    assert buscar_producto(inventario, "P999") is None


def test_cp12_menu_completo(capsys):
    """CP12 - Menú registrar y consultar"""
    respuestas = iter(["1", "P001", "Teclado", "350", "10", "2", "0"])
    inventario = menu(entrada=lambda _: next(respuestas))
    salida = capsys.readouterr().out
    assert len(inventario) == 1
    assert "Producto P001 registrado." in salida
    assert "Precio: $350.00" in salida
