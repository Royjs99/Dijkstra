import heapq
import matplotlib.pyplot as plt
import networkx as nx

def dijkstra(grafo, inicio):
    # Cola de prioridad para almacenar los nodos a explorar
    cola = []
    heapq.heappush(cola, (0, inicio))  # (distancia, nodo)

    # Diccionario para guardar las distancias más cortas desde el inicio
    distancias = {nodo: float('inf') for nodo in grafo}
    distancias[inicio] = 0

    # Diccionario para guardar el camino anterior de cada nodo
    nodos_anteriores = {nodo: None for nodo in grafo}

    while cola:
        # Obtener el nodo con la menor distancia
        distancia_actual, nodo_actual = heapq.heappop(cola)

        # Explorar vecinos
        for vecino, peso in grafo[nodo_actual].items():
            distancia = distancia_actual + peso

            # Si se encuentra un camino más corto
            if distancia < distancias[vecino]:
                distancias[vecino] = distancia
                nodos_anteriores[vecino] = nodo_actual
                heapq.heappush(cola, (distancia, vecino))

    return distancias, nodos_anteriores

def reconstruir_camino(nodos_anteriores, inicio, destino):
    camino = []
    nodo_actual = destino
    while nodo_actual is not None:
        camino.append(nodo_actual)
        nodo_actual = nodos_anteriores[nodo_actual]
    camino.reverse()
    return camino

def dibujar_grafo(grafo, camino=None):
    G = nx.Graph()
    
    # Agregar las conexiones al grafo
    for nodo in grafo:
        for vecino, peso in grafo[nodo].items():
            G.add_edge(nodo, vecino, weight=peso)
    
    # Definir posiciones fijas para los nodos
    posiciones = {
        'A': (-1, 0),   # Nodo A a la izquierda y centrado
        'B': (0, 1),
        'C': (1, 1),
        'D': (0, -1),
        'E': (1, 0),
        'F': (2, 1),
        'G': (2, 0),
        'H': (3, 0)
    }
    
    etiquetas_aristas = nx.get_edge_attributes(G, 'weight')
    
    # Dibujar el grafo
    nx.draw(G, posiciones, with_labels=True, node_color='lightblue', node_size=500, font_size=12)
    nx.draw_networkx_edge_labels(G, posiciones, edge_labels=etiquetas_aristas)
    
    # Si se proporciona un camino, resaltarlo
    if camino:
        aristas_camino = [(camino[i], camino[i+1]) for i in range(len(camino)-1)]
        nx.draw_networkx_edges(G, posiciones, edgelist=aristas_camino, edge_color='r', width=2)
    
    plt.show()


# Ejemplo de grafo
grafo = {
    'A': {'B': 2, 'C': 5, 'D': 1},
    'B': {'A': 2, 'C': 3, 'E': 4},
    'C': {'A': 5, 'B': 3, 'F': 6},
    'D': {'A': 1, 'E': 7},
    'E': {'B': 4, 'D': 7, 'F': 8, 'G': 2},
    'F': {'C': 6, 'E': 8, 'G': 3},
    'G': {'E': 2, 'F': 3, 'H': 1},
    'H': {'G': 1}
}


# Ejecutar Dijkstra desde 'A'
distancias, nodos_anteriores = dijkstra(grafo, 'A')

# Imprimir los caminos más cortos desde A a todos los nodos
for nodo in grafo:
    camino = reconstruir_camino(nodos_anteriores, 'A', nodo)
    print(f"Camino más corto desde A hasta {nodo}: {distancias[nodo]} (Ruta: {' -> '.join(camino)})")

# Reconstruir el camino desde 'A' hasta 'D'
camino = reconstruir_camino(nodos_anteriores, 'A', 'D')
print(f"Camino desde A hasta D: {camino}")

# Visualizar el grafo y el camino más corto de A a D
dibujar_grafo(grafo, camino)
