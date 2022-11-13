from scipy.optimize import linprog, OptimizeResult

def ingresarMatriz(filas: int, columnas: int):
    matriz = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            fila.append(float(input(f"Ingrese valor de la posición {i}, {j}: ")))
        matriz.append(fila)
    return matriz

def mostrarMatriz(matriz):
    for fila in matriz:
        print(f"\t{fila}")

def generarFuncion(cantEstrategias):
    funcion = [-1]
    for i in range(cantEstrategias):
        funcion.append(0)
    return funcion

def generarLimites(cantEstrategias):
    limites = ((None, None),)
    for i in range(cantEstrategias):
        limites = (*limites, (0, None))
    return limites

def generarRestriccionesJ1(premios):
    # generacion de las restricciones con desigualdades
    lado_izq_ineq = []
    lado_der_ineq = []
    
    for j in range(len(premios[0])):
        coeficientes = [1]
        for i in range(len(premios)):
            coeficientes.append(-1 * premios[i][j])
        lado_izq_ineq.append(coeficientes)

    for i in range(len(premios)):
        lado_der_ineq.append(0)

    # generacion de las restricciones con igualdades
    lado_izq_eq = [0]
    lado_der_eq = [1]

    for i in range(len(premios)):
        lado_izq_eq.append(1)

    return lado_izq_ineq, lado_der_ineq, [lado_izq_eq], lado_der_eq

def generarRestriccionesJ2(premios):
    # generacion de las restricciones con desigualdades
    lado_izq_ineq = []
    lado_der_ineq = []
    
    for i in range(len(premios)):
        coeficientes = [1]
        for j in range(len(premios[0])):
            coeficientes.append(-1 * premios[i][j])
        lado_izq_ineq.append(coeficientes)

    for i in range(len(premios[0])):
        lado_der_ineq.append(0)

    # generacion de las restricciones con igualdades
    lado_izq_eq = [0]
    lado_der_eq = [1]

    for i in range(len(premios[0])):
        lado_izq_eq.append(1)

    return lado_izq_ineq, lado_der_ineq, [lado_izq_eq], lado_der_eq

def resolverJ1(premios):
    funcion = generarFuncion(len(premios))
    limites = generarLimites(len(premios))
    lado_izq_ineq, lado_der_ineq, lado_izq_eq, lado_der_eq = generarRestriccionesJ1(premios)

    return linprog(funcion, lado_izq_ineq, lado_der_ineq, lado_izq_eq, lado_der_eq, bounds=limites, method="highs")

def resolverJ2(premios):
    funcion = generarFuncion(len(premios[0]))
    limites = generarLimites(len(premios[0]))
    lado_izq_ineq, lado_der_ineq, lado_izq_eq, lado_der_eq = generarRestriccionesJ2(premios)

    return linprog(funcion, lado_izq_ineq, lado_der_ineq, lado_izq_eq, lado_der_eq, bounds=limites, method="highs")


filas = int(input(f"Ingrese la cantidad de estrategias para el jugador 1: "))
columnas = int(input(f"Ingrese la cantidad de estrategias para el jugador 2: "))

print(f"Ingrese la matriz de premios: ")
m = ingresarMatriz(filas, columnas)
# m = [
#     [3, -1, -3],
#     [-2, 4, -1],
#     [-5, -6, 2]
# ]

print("Matriz de premios:")
mostrarMatriz(m)

resultadoJ1: OptimizeResult = resolverJ1(m)
resultadoJ2: OptimizeResult = resolverJ2(m)

print("Resultados para el jugador 1: ")
for index, res in enumerate(resultadoJ1["x"]):
    if(index == 0):
        print(f"\tv = {round(res, 2)}")
    else:
        print(f"\tx{index} = {round(res, 2)}")

print("Resultados para el jugador 2: ")
for index, res in enumerate(resultadoJ2["x"]):
    if(index == 0):
        print(f"\tv = {round(res, 2)}")
    else:
        print(f"\ty{index} = {round(res, 2)}")