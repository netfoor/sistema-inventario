# Historial de versiones

## v1.1.0 - 2026-11-17

- Nuevo `src/main.py`: menú de consola para registrar, consultar y buscar productos por código.
- No permite registrar dos productos con el mismo código.
- Pruebas CP08 a CP12 para el registro, la consulta, la búsqueda y el menú.

## v1.0.2 - 2026-11-17

- Corrección: `mostrar_informacion()` vuelve a mostrar el nombre del producto tal como se registró.
- Las 7 pruebas de la funcionalidad Producto pasan de nuevo y la versión se publica en GitHub Releases.

## v1.0.1 - 2026-11-17 (no publicada)

- Cambio intencional para la práctica RELEASE: el nombre se mostraba en mayúsculas.
- Fallaron CP03, CP06 y CP07; el workflow de liberación se detuvo en las pruebas y no publicó la versión.

## v1.0.0 - 2026-11-17

- Primera versión del Sistema de Inventario.
- Clase `Producto` con código, nombre, precio y existencia, y el método `mostrar_informacion()`.
- Pruebas automatizadas con pytest (CP01 a CP07) y workflows de pruebas, construcción y liberación en GitHub Actions.
