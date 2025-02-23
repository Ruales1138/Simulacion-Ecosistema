import random

class Depredador:
    def __init__(self):
        self.energia = 5
    
    def __repr__(self):
        return 'Depredador'
    
class Presa:
    def __init__(self):
        self.energia = 5

    def __repr__(self):
        return 'Presa'
    
class Planta:
    def __init__(self):
        self.energia = 5

    def __repr__(self):
        return 'Planta'
    

def generar_matriz(n: int, i: int = 0, j: int = 0, matriz: list[list[int]] = [], fila: list[int] = []) -> list[list[int]]:
    if i == n:
        return matriz
    
    if j == n:
        matriz.append(fila)
        return generar_matriz(n, i+1, 0, matriz, [])
    
    elemento = random.choice([Depredador(), Presa(), Planta()])
    fila.append(random.choice([elemento, '   ']))
    return generar_matriz(n, i, j+1, matriz, fila)


print(generar_matriz(5))
lobo = Depredador()
print(lobo)