import math


def es_primo(numero: int) -> bool:
    """Determina si un número entero es primo."""
    if numero < 2:
        return False
    if numero == 2:
        return True
    if numero % 2 == 0:
        return False

    limite = math.isqrt(numero) + 1
    for divisor in range(3, limite, 2):
        if numero % divisor == 0:
            return False
    return True