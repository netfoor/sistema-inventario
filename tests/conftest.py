"""Imprime un resumen por caso de prueba al terminar la ejecución."""

import pytest

resultados = []


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    reporte = (yield).get_result()
    if reporte.when == "call":
        nombre = (item.function.__doc__ or item.name).strip()
        resultados.append((nombre, "CORRECTO" if reporte.passed else "ERROR"))


def pytest_terminal_summary(terminalreporter):
    if not resultados:
        return
    tr = terminalreporter
    tr.section("RESULTADOS DE LAS PRUEBAS")
    for nombre, estado in resultados:
        tr.write_line(f"{nombre:<34}{estado}")
    correctas = sum(estado == "CORRECTO" for _, estado in resultados)
    tr.write_line(f"Resultado: {correctas} de {len(resultados)} pruebas satisfactorias.")
