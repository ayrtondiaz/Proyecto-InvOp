def load_graph(c_arcos):
    graph = []
    for i in range(c_arcos):
        edge = []
        weight = int(input('Ingresar Peso: '))
        edge.append(weight)
        source_node = int(input('Ingresar Nodo Origen: '))
        edge.append(source_node)
        destiny_node = int(input('Ingresar Nodo Destino: '))
        edge.append(destiny_node)

        graph.append(edge)
    # Now, we order the items by non decreasing order and return it
    graph = sorted(graph, key=lambda item: item[0])
    return graph

def MST(graph,q_edges):
    result_graph = []
    connected_nodes = []
    not_connected_nodes = []

    # In this step we going to create connected_nodes and not connected nodes yet
    for node in range(q_edges):
        connected_nodes.append(node)
        not_connected_nodes.append(0)
    # while numbers of edges are distinct to q_edges-1
    iterations = 0
    index = 0
    while(iterations<(q_edges-1)):
        weight = graph[iterations][0]
        source_node = graph[iterations][1]
        destiny_node = graph[iterations][2]
        iterations += 1
        #verify that the conexion dont get a cycle
        x = find(connected_nodes, source_node)
        y = find(connected_nodes, destiny_node)
        if x != y:
            index += 1
            result_graph.append([weight, source_node, destiny_node])
            union(connected_nodes, not_connected_nodes, x, y)
    minimum_cost = 0
    print("Árbol de Mínima Expansión")
    for item in result_graph:
        weight = item[0]
        source_node =item[1]
        destiny_node = item[2]
        minimum_cost += weight
        print('(Peso) | origen --> destino')
        print("(%d) | %d --> %d " % (weight, source_node, destiny_node))
    print("Longitud mínima Total del Grafo: ", minimum_cost)


def find(connected_nodes, i):
    if connected_nodes[i] != i:
        connected_nodes[i] = find(connected_nodes, connected_nodes[i])
    return connected_nodes[i]

def union(connected_nodes, not_connected_nodes, x, y):
        if not_connected_nodes[x] < not_connected_nodes[y]:
            connected_nodes[x] = y
        elif not_connected_nodes[x] > not_connected_nodes[y]:
            connected_nodes[y] = x
        else:
            connected_nodes[y] = x
            not_connected_nodes[x] += 1

def main():
    q_edges = int(input('Ingresar Cantidad de Arcos: '))
    print('\nCargar Grafo')
    graph = load_graph(q_edges)
    print('\nNuestro Grafo es:')
    print (graph)
    print('\Solución:')
    MST(graph,q_edges)
main()