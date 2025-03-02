import random

class Depredador:
    def __init__(self):
        self.energia: int = 5
    
    def __repr__(self):
        return '🦁 '
    
class Presa:
    def __init__(self):
        self.energia: int = 5

    def __repr__(self):
        return '🦓 '
    
class Planta:
    def __init__(self):
        self.energia: int = 5

    def __repr__(self):
        return '🌾 '
    

def generar_matriz(n: int, i: int = 0, j: int = 0, matriz: list[list[int]] = [], fila: list[int] = []) -> list[list[int]]:
    if i == n:
        return matriz
    
    if j == n:
        matriz.append(fila)
        return generar_matriz(n, i+1, 0, matriz, [])
    
    elemento = random.choice([Depredador(), Presa(), Planta()])
    fila.append(random.choice([elemento, ' ']))
    return generar_matriz(n, i, j+1, matriz, fila)


ecosistema = generar_matriz(5)

print(*ecosistema, sep="\n")
print('-----------------------------------Ciclo')


def buscar_presa(ecosistema, fila, columna, paso=1):
    if paso >= len(ecosistema):
        return (-1, -1)
    
    if fila + paso < len(ecosistema) and isinstance(ecosistema[fila + paso][columna], Presa):
        return (fila + paso, columna)
    if fila - paso >= 0 and isinstance(ecosistema[fila - paso][columna], Presa):
        return (fila - paso, columna) 
    
    if columna + paso < len(ecosistema) and isinstance(ecosistema[fila][columna + paso], Presa):
        return (fila, columna + paso)
    if columna - paso >=0 and isinstance(ecosistema[fila][columna - paso], Presa):
        return (fila, columna - paso)
    
    return buscar_presa(ecosistema, fila, columna, paso+1) 


def mover_depredador(ecosistema, fila, columna):
    presa = buscar_presa(ecosistema, fila, columna)

    if presa != (-1, -1):
        fila_p, columna_p = presa
        ecosistema[fila_p][columna_p] = Depredador()
        ecosistema[fila][columna] = ' '

    if presa == (-1, -1):
        fila_o_columna = random.randint(0,1)
        print(fila_o_columna)

        if fila_o_columna == 0:
            fila_a = random.randint(0, len(ecosistema)-1)
            print(fila_a)
            if ecosistema[fila_a][columna] == ' ':
                ecosistema[fila_a][columna] = Depredador()
                ecosistema[fila][columna] = ' '

        if fila_o_columna == 1:
            columna_a = random.randint(0, len(ecosistema)-1)
            print(columna_a)
            if ecosistema[fila][columna_a] == ' ':
                ecosistema[fila][columna_a] = Depredador()
                ecosistema[fila][columna] = ' '
            
        print('No hay presa')

    return ecosistema


def actualizar_ecosistema(ecosistema: list[list[object]], fila: int = 0, columna: int = 0) -> tuple:
    if fila == len(ecosistema):
        return 'Fin'
    
    if columna == len(ecosistema):
        return actualizar_ecosistema(ecosistema, fila+1, 0)
    
    if isinstance(ecosistema[fila][columna], Depredador):
        print(f'D{fila, columna}')
        ecosistema = mover_depredador(ecosistema, fila, columna)
        print(*ecosistema, sep="\n")

    if isinstance(ecosistema[fila][columna], Presa):
        print(f'P{fila, columna}')
        print(*ecosistema, sep="\n")

    return actualizar_ecosistema(ecosistema, fila, columna+1)
    
print (actualizar_ecosistema(ecosistema))


def ciclos(ecosistema: list[list[str]], idx: int = 0, limite: int = 5) -> None:
    if idx == limite:
        return 'Fin del ciclo'
    else:
        print(*ecosistema, sep="\n")
        print('-----------------------------------')
        return ciclos(ecosistema, idx+1)

# print(ciclos(ecosistema))