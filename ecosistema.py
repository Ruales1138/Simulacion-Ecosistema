import random

def generar_matriz(n: int, i: int = 0, j: int = 0, matriz: list[list[int]] = [], fila: list[int] = []) -> list[list[int]]:
    if i == n:
        return matriz
    if j == n:
        matriz.append(fila)
        return generar_matriz(n, i+1, 0, matriz, [])
    fila.append(random.randint(1, 100))
    return generar_matriz(n, i, j+1, matriz, fila)

print(generar_matriz(5))