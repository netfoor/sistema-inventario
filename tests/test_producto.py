"""Pruebas de la funcionalidad Producto (fase TEST)."""

import pytest

from producto import Producto


@pytest.fixture
def teclado():
    return Producto("P001", "Teclado", 350, 10)


def mostrar(producto, capsys):
    """Ejecuta mostrar_informacion() y devuelve lo que imprimió."""
    producto.mostrar_informacion()
    return capsys.readouterr().out


def test_cp01_crear_producto(teclado):
    """CP01 - Crear producto"""
    assert isinstance(teclado, Producto)
    assert (teclado.codigo, teclado.nombre, teclado.precio, teclado.existencia) == (
        "P001",
        "Teclado",
        350,
        10,
    )


def test_cp02_mostrar_codigo(teclado, capsys):
    """CP02 - Mostrar código"""
    assert teclado.codigo == "P001"
    assert "Código: P001" in mostrar(teclado, capsys)


def test_cp03_mostrar_nombre(teclado, capsys):
    """CP03 - Mostrar nombre"""
    assert teclado.nombre == "Teclado"
    assert "Nombre: Teclado" in mostrar(teclado, capsys)


def test_cp04_mostrar_precio(teclado, capsys):
    """CP04 - Mostrar precio"""
    assert teclado.precio == 350
    assert "Precio: $350.00" in mostrar(teclado, capsys)


def test_cp05_mostrar_existencia(teclado, capsys):
    """CP05 - Mostrar existencia"""
    assert teclado.existencia == 10
    assert "Existencia: 10 unidades" in mostrar(teclado, capsys)


def test_cp06_mostrar_informacion_completa(teclado, capsys):
    """CP06 - Mostrar información"""
    lineas = mostrar(teclado, capsys).splitlines()
    assert lineas[:4] == [
        "Código: P001",
        "Nombre: Teclado",
        "Precio: $350.00",
        "Existencia: 10 unidades",
    ]


def test_cp07_crear_segundo_producto(teclado, capsys):
    """CP07 - Crear segundo producto"""
    mouse = Producto("P002", "Mouse", 180, 5)
    salida_mouse = mostrar(mouse, capsys)
    salida_teclado = mostrar(teclado, capsys)
    assert (mouse.codigo, mouse.nombre, mouse.precio, mouse.existencia) == (
        "P002",
        "Mouse",
        180,
        5,
    )
    assert "Nombre: Mouse" in salida_mouse and "Teclado" not in salida_mouse
    assert "Nombre: Teclado" in salida_teclado and "Mouse" not in salida_teclado
