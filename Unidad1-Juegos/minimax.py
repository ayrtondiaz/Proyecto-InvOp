import numpy as np
from sys import stdout

class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    END = '\033[0m'

def echo(string, end='\r\n', color=None):
    if color:
        stdout.write("%s%s%s" % (
            color,
            string,
            Colors.END
        ))
    else:
        stdout.write(string)
    if end: 
        stdout.write("\n")


def cargarPagos(cant):
    vec1 = []
    for i in range(cant):
        vec2 = []
        for j in range(cant):
            echo(
                f'ingrese el pago de la celda [{i+1},{j+1}]:', color=Colors.GREEN, end='')
            pago = int(input())
            vec2.append(pago)
        vec1.append(vec2)
    return vec1

def maximin(arreglo):
    max = arreglo[0][0]
    list = []
    for i in range(len(arreglo)):
        for j in range(len(arreglo[i])):
            if (max > arreglo[i][j]):
                max = arreglo[i][j]
        list.append(max)
        max = 0
    return list


def minimax(arreglo):
    min = arreglo[0][0]
    list = []
    for i in range(len(arreglo)):
        for j in range(len(arreglo[i])):
            if (min < arreglo[j][i]):
                min = arreglo[j][i]
        list.append(min)
        min = 0
    return list


def maximoMinimos(a):
    max = a[0]
    for i in range(len(a)):
        if (max < a[i]):
            max = a[i]
    return max


def minimoMaximos(a):
    min = a[0]
    for i in range(len(a)):
        if (min > a[i]):
            min = a[i]
    return min


def equilibrio(a, b):
    if (a == b):
        echo('punto silla', color=Colors.GREEN,end='')
        echo(f' => {a}', color=Colors.YELLOW)
    else:
        echo('juego inestable', color=Colors.RED)




def main():
    echo('Maximin y Minimax', color=Colors.GREEN, end='')    
    echo('\nIngrese numero de estrategias:', color=Colors.BLUE, end='')
    cantEstrategias = int(input())
    estrategJ1 = cargarPagos(cantEstrategias)
    echo('\nMatriz de estrategias', color=Colors.RED, end='')
    matEstrategias = np.array(estrategJ1)
    print(matEstrategias)
    minimos = maximin(matEstrategias)
    maximos = minimax(matEstrategias)
    max = maximoMinimos(minimos)
    min = minimoMaximos(maximos)
    echo('Resultado:', color=Colors.RED, end='')
    equilibrio(max, min)
        


main()