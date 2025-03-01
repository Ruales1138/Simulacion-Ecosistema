import random

class Depredador:
    def __init__(self):
        self.energia: int = 5
    
    def __repr__(self):
        return 'D '
    
class Presa:
    def __init__(self):
        self.energia: int = 5

    def __repr__(self):
        return 'P '
    
class Planta:
    def __init__(self):
        self.energia: int = 5

    def __repr__(self):
        return 'C '
    

def generar_matriz(n: int, i: int = 0, j: int = 0, matriz: list[list[int]] = [], fila: list[int] = []) -> list[list[int]]:
    if i == n:
        return matriz
    
    if j == n:
        matriz.append(fila)
        return generar_matriz(n, i+1, 0, matriz, [])
    
    elemento = random.choice([Depredador(), Presa(), Planta()])
    fila.append(random.choice([elemento, '']))
    return generar_matriz(n, i, j+1, matriz, fila)


ecosistema = generar_matriz(5)

print(*ecosistema, sep="\n")
print('-----------------------------------Ciclo')


def buscar_presa(ecosistema, fila, columna, paso=1):
    if fila + paso == len(ecosistema) or columna + paso == len(ecosistema):
        return
    if isinstance(ecosistema[fila][columna + paso], Presa):
        print(fila, columna + paso)
        return (fila, columna + paso)
    if isinstance(ecosistema[fila + paso][columna], Presa):
        print(fila + paso, columna)
        return (fila + paso, columna)
    return buscar_presa(ecosistema, fila, columna, paso+1)


def mover_depredador(ecosistema, fila, columna):
    presa = buscar_presa(ecosistema, fila, columna)
    ecosistema[fila][columna] = ''
    return ecosistema


def actualizar_ecosistema(ecosistema: list[list[object]], elemento: type, fila: int = 0, columna: int = 0) -> tuple:
    if fila == len(ecosistema):
        return 'Fin'
    if columna == len(ecosistema):
        return actualizar_ecosistema(ecosistema, elemento, fila+1, 0)
    if isinstance(ecosistema[fila][columna], elemento):
        ecosistema = mover_depredador(ecosistema, fila, columna)
        print(fila, columna)
        print(*ecosistema, sep="\n")
    return actualizar_ecosistema(ecosistema, elemento, fila, columna+1)
    
print (actualizar_ecosistema(ecosistema, Depredador))


def ciclos(ecosistema: list[list[str]], idx: int = 0, limite: int = 5) -> None:
    if idx == limite:
        return 'Fin del ciclo'
    else:
        print(*ecosistema, sep="\n")
        print('-----------------------------------')
        return ciclos(ecosistema, idx+1)

# print(ciclos(ecosistema))