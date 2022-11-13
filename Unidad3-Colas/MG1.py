
lam = float(input("Ingrese la tasa de llegada (lambda): "))
mu = float(input("Ingrese la tasa de servicio (mu): "))
varianza = float(input("Ingrese la varianza de la distribución del servicio: "))

# Factor de utilizacion del servidor
rho = lam / mu

# Cantidad promedio en cola
Lq = ((lam**2 * varianza) + rho**2) / (2 * (1-rho))

# Cantidad promedio en el sistema
L = Lq + rho

# Tiempo promedio en cola
Wq = Lq/lam

# Tiempo promedio en el sistema
W = Wq + 1/mu

print("Medidas de Eficacia del Sistema:")
print(f"\tCantidad promedio en el sistema: L = {L}")
print(f"\tCantidad promedio esperando en la cola: Lq = {Lq}")
print(f"\tTiempo promedio en el sistema: W = {W}")
print(f"\tTiempo promedio esperando en la cola: W = {Wq}")
print(f"\tFactor de utilización del unico servidor: rho = {rho}")