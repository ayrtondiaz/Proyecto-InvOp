import numpy as np
def factorial(num): 
    if num < 0: 
        raise Exception('Nro Negativo!')
    elif num == 0: 
        return 1
    else: 
        fact = 1
        while(num > 1): 
            fact *= num 
            num -= 1
        return fact 

lamda = int(input("Lambda: "))
mu = int(input("Mu: "))
s = int(input("Servidores: "))

P = []
C = []

rho = lamda/mu
P0 = 1-rho
Lq = (P0*((lamda/mu)**s)*rho/(factorial(s)*((P0)**2)))  
Wq = Lq / lamda
W = Wq + (1/mu)
L = Lq + (lamda/mu)

P.append(P0)
pacum = []
for i in range(1, 40):
    Pn = P[-1]
    if(i<=0 and i<=s):
        Pi = (((lamda/mu)**i)/factorial(i))*Pn
    else:
        Pi = (((lamda/mu)**i)/(factorial(s)*(s**(i-s))))*Pn
    P.append(Pi)
    pacum.append(sum(P))

print(f'lambda: {lamda}')
print(f'Mu: {mu}')
print(f'c: {s}')
print(f'Wq: {Wq}')
print(f'Lq: {Lq}')
print(f'L: {L}')
print(f'W: {W}')
print(np.array(P))