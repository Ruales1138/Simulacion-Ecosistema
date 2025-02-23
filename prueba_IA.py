import random

class Depredador:
    def __init__(self, energia=5):
        self.energia = energia
    
    def __repr__(self):
        return 'D'
    
class Presa:
    def __init__(self, energia=5):
        self.energia = energia
    
    def __repr__(self):
        return 'P'
    
class Planta:
    def __init__(self):
        self.energia = 5
    
    def __repr__(self):
        return 'V'

def generar_matriz(n, i=0, matriz=None):
    if matriz is None:
        matriz = []
    if i == n:
        return matriz
    fila = generar_fila(n)
    return generar_matriz(n, i + 1, matriz + [fila])

def generar_fila(n, j=0, fila=None):
    if fila is None:
        fila = []
    if j == n:
        return fila
    elemento = random.choice([Depredador(), Presa(), Planta(), None])
    return generar_fila(n, j + 1, fila + [elemento])

def imprimir_matriz(matriz, i=0):
    if i == len(matriz):
        return
    print(' '.join(str(e) if e else '.' for e in matriz[i]))
    imprimir_matriz(matriz, i + 1)

def simular_ecosistema(matriz, ciclos, ciclo_actual=0):
    if ciclo_actual == ciclos or not hay_organismos(matriz):
        return matriz
    matriz = actualizar_matriz(matriz)
    imprimir_matriz(matriz)
    print("-")
    return simular_ecosistema(matriz, ciclos, ciclo_actual + 1)

def hay_organismos(matriz, i=0, j=0):
    if i == len(matriz):
        return False
    if j == len(matriz[i]):
        return hay_organismos(matriz, i + 1, 0)
    if isinstance(matriz[i][j], (Depredador, Presa)):
        return True
    return hay_organismos(matriz, i, j + 1)

def actualizar_matriz(matriz, i=0):
    if i == len(matriz):
        return matriz
    matriz[i] = actualizar_fila(matriz, i)
    return actualizar_matriz(matriz, i + 1)

def actualizar_fila(matriz, i, j=0, nueva_fila=None):
    if nueva_fila is None:
        nueva_fila = []
    if j == len(matriz[i]):
        return nueva_fila
    elemento = matriz[i][j]
    nuevo_elemento = procesar_elemento(elemento, matriz, i, j)
    return actualizar_fila(matriz, i, j + 1, nueva_fila + [nuevo_elemento])

def procesar_elemento(elemento, matriz, i, j):
    if isinstance(elemento, Depredador):
        return mover_depredador(elemento, matriz, i, j)
    if isinstance(elemento, Presa):
        return mover_presa(elemento, matriz, i, j)
    return elemento

def mover_depredador(dep, matriz, i, j):
    presa_pos = buscar_presa(matriz, i, j)
    if presa_pos:
        matriz[presa_pos[0]][presa_pos[1]] = dep
        return None
    return dep

def buscar_presa(matriz, i, j, d=1):
    if d >= len(matriz):
        return None
    if j + d < len(matriz[i]) and isinstance(matriz[i][j + d], Presa):
        return (i, j + d)
    if j - d >= 0 and isinstance(matriz[i][j - d], Presa):
        return (i, j - d)
    return buscar_presa(matriz, i, j, d + 1)

def mover_presa(presa, matriz, i, j):
    return presa

n = 5
ciclos = 10
ecosistema = generar_matriz(n)
imprimir_matriz(ecosistema)
print("Inicio de la simulación")
simular_ecosistema(ecosistema, ciclos)
