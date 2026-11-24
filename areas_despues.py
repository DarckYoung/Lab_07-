import math


def calcular_area_circulo(radio: float) -> float:
    return math.pi * (radio ** 2)


def calcular_area_rectangulo(base: float, altura: float) -> float:
    return base * altura


def calcular_area_triangulo(base: float, altura: float) -> float:
    return (base * altura) / 2


def mostrar_area(nombre_figura: str, area: float) -> None:
    print(f"El área del {nombre_figura} es: {area:.2f}")


if __name__ == "__main__":
    mostrar_area("círculo", calcular_area_circulo(5))
    mostrar_area("rectángulo", calcular_area_rectangulo(10, 4))
    mostrar_area("triángulo", calcular_area_triangulo(6, 3))