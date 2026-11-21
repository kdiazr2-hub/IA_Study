"""
Diagnóstico inicial de Python.

Completa cada función (sustituye `raise NotImplementedError` por tu código)
y ejecuta:

    python 01_python/00_diagnostico.py

Al final verás cuántos ejercicios pasan. No busques las respuestas:
lo que no sepas hacer nos indica por dónde empezar.
"""


# 1. Cadenas
def invertir_palabras(frase):
    """Devuelve la frase con el orden de las palabras invertido.
    invertir_palabras("hola mundo cruel") -> "cruel mundo hola"
    """
    raise NotImplementedError


# 2. Listas y bucles
def pares_al_cuadrado(numeros):
    """Devuelve una lista con el cuadrado de los números pares, en el mismo orden.
    pares_al_cuadrado([1, 2, 3, 4]) -> [4, 16]
    """
    raise NotImplementedError


# 3. Diccionarios
def contar_letras(texto):
    """Devuelve un diccionario {letra: veces} solo con letras, en minúsculas.
    contar_letras("Ana") -> {"a": 2, "n": 1}
    """
    raise NotImplementedError


# 4. Condicionales
def clasificar_nota(nota):
    """0-4.9 -> "suspenso", 5-6.9 -> "aprobado", 7-8.9 -> "notable", 9-10 -> "sobresaliente".
    Si la nota no está entre 0 y 10, lanza ValueError.
    """
    raise NotImplementedError


# 5. Funciones con argumentos por defecto
def saludar(nombre, saludo="Hola", exclamacion=False):
    """saludar("Ana") -> "Hola, Ana"
    saludar("Ana", "Buenas", exclamacion=True) -> "Buenas, Ana!"
    """
    raise NotImplementedError


# 6. Tuplas y ordenación
def ordenar_por_edad(personas):
    """Recibe una lista de tuplas (nombre, edad) y la devuelve ordenada por edad,
    de menor a mayor.
    ordenar_por_edad([("Ana", 30), ("Luis", 25)]) -> [("Luis", 25), ("Ana", 30)]
    """
    raise NotImplementedError


# 7. Conjuntos
def elementos_comunes(a, b):
    """Devuelve una lista ORDENADA de los elementos que están en ambas listas, sin repetir.
    elementos_comunes([1, 2, 2, 3], [2, 3, 4]) -> [2, 3]
    """
    raise NotImplementedError


# 8. Recursión
def factorial(n):
    """factorial(5) -> 120, factorial(0) -> 1. Hazlo con recursión."""
    raise NotImplementedError


# 9. Clases
class CuentaBancaria:
    """Una cuenta con titular y saldo (que empieza en 0).

    c = CuentaBancaria("Ana")
    c.depositar(100)
    c.retirar(30)
    c.saldo -> 70
    c.retirar(1000)  -> lanza ValueError("Saldo insuficiente")
    """

    def __init__(self, titular):
        raise NotImplementedError

    def depositar(self, cantidad):
        raise NotImplementedError

    def retirar(self, cantidad):
        raise NotImplementedError


# 10. Comprensiones de diccionario
def invertir_diccionario(d):
    """Intercambia claves y valores.
    invertir_diccionario({"a": 1, "b": 2}) -> {1: "a", 2: "b"}
    """
    raise NotImplementedError


# ---------------------------------------------------------------------------
# Pruebas automáticas: no hace falta tocar nada de aquí hacia abajo.
# ---------------------------------------------------------------------------

def _prueba_cuenta():
    c = CuentaBancaria("Ana")
    c.depositar(100)
    c.retirar(30)
    assert c.titular == "Ana"
    assert c.saldo == 70
    try:
        c.retirar(1000)
    except ValueError:
        pass
    else:
        raise AssertionError("retirar(1000) debería lanzar ValueError")
    assert c.saldo == 70


def _prueba_nota():
    assert clasificar_nota(4.9) == "suspenso"
    assert clasificar_nota(5) == "aprobado"
    assert clasificar_nota(7.5) == "notable"
    assert clasificar_nota(10) == "sobresaliente"
    for mala in (-1, 11):
        try:
            clasificar_nota(mala)
        except ValueError:
            pass
        else:
            raise AssertionError(f"clasificar_nota({mala}) debería lanzar ValueError")


PRUEBAS = [
    ("1. invertir_palabras", lambda: invertir_palabras("hola mundo cruel") == "cruel mundo hola"),
    ("2. pares_al_cuadrado", lambda: pares_al_cuadrado([1, 2, 3, 4, 6]) == [4, 16, 36]),
    ("3. contar_letras", lambda: contar_letras("Ana, ana!") == {"a": 4, "n": 2}),
    ("4. clasificar_nota", lambda: _prueba_nota() is None),
    ("5. saludar", lambda: saludar("Ana") == "Hola, Ana"
        and saludar("Ana", "Buenas", exclamacion=True) == "Buenas, Ana!"),
    ("6. ordenar_por_edad", lambda: ordenar_por_edad([("Ana", 30), ("Luis", 25), ("Eva", 40)])
        == [("Luis", 25), ("Ana", 30), ("Eva", 40)]),
    ("7. elementos_comunes", lambda: elementos_comunes([3, 1, 2, 2], [2, 3, 4]) == [2, 3]),
    ("8. factorial", lambda: factorial(0) == 1 and factorial(5) == 120),
    ("9. CuentaBancaria", lambda: _prueba_cuenta() is None),
    ("10. invertir_diccionario", lambda: invertir_diccionario({"a": 1, "b": 2}) == {1: "a", 2: "b"}),
]


if __name__ == "__main__":
    aprobadas = 0
    for nombre, prueba in PRUEBAS:
        try:
            ok = prueba()
            estado = "OK" if ok else "FALLA (resultado incorrecto)"
        except NotImplementedError:
            ok, estado = False, "pendiente"
        except Exception as e:  # noqa: BLE001
            ok, estado = False, f"ERROR: {type(e).__name__}: {e}"
        aprobadas += bool(ok)
        print(f"{'✔' if ok else '✘'} {nombre:28} {estado}")
    print(f"\n{aprobadas}/{len(PRUEBAS)} ejercicios correctos")
