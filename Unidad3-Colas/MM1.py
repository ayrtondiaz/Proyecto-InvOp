INF = 99999999999999

def load_data():
    lamda = int(input('Ingresar Tasa de Llegada Lamda: '))
    mu = int(input('Ingresar Tasa de Servicio Mu: '))
    q_server = int(input('Ingresar Cantidad de Servidores c: '))
    try:
        q_system_lim = int(input('Ingresar Límite Sistema: '))
    except:
        q_system_lim = INF
    try:
        q_source_lim = int(input('Ingresar Límite Fuente: '))
    except:
        q_source_lim = INF
    return lamda, mu, q_server, q_system_lim, q_source_lim
def main():
    lamda, mu, q_server, q_system_lim, q_source_lim = load_data()
    MM1(lamda, mu, q_server, q_system_lim, q_source_lim)
    
def MM1(lamda, mu, q_server, q_system_lim, q_source_lim):
    Probabilidades = []
    roh = lamda / mu 
    Ls = lamda / (mu-lamda)
    Wq = lamda/(mu*(mu-lamda))
    Lq = Wq * lamda
    Ws = 1 / (mu - lamda)
    c = roh
    P0 = 1-roh
    Probabilidades.append(P0)
    for i in range(1,40):
        Ultimo_P = Probabilidades[-1]
        Nuevo_P = Ultimo_P * roh
        Probabilidades.append(Nuevo_P)
    for index, value in enumerate(Probabilidades):
        print('Index:', index, ' Value: ', '{:f}'.format(value))

main()