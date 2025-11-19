# dijkstra_simulador.py
import heapq
import time

def print_estado(dist, prev, visitados, pq):
    print("Distancias actuales:")
    for v in sorted(dist):
        d = dist[v]
        pd = "∞" if d == float('inf') else d
        p = prev[v] if prev[v] is not None else "-"
        mark = " (visitado)" if v in visitados else ""
        print(f"  {v}: {pd}\tprev: {p}{mark}")
    print("Cola de prioridad (heap):", pq)
    print("-" * 50)

def dijkstra_step_by_step(graph, inicio, mostrar_pausa=True, pausa=0.8):
    """
    graph: dict nodo -> list of (vecino, peso)
    inicio: nodo inicial
    mostrar_pausa: si True hace time.sleep entre pasos para ver la salida
    """
    # Inicialización
    dist = {v: float('inf') for v in graph}
    prev = {v: None for v in graph}
    dist[inicio] = 0

    visitados = set()
    heap = [(0, inicio)]  # (distancia, nodo)

    print(f"Iniciando Dijkstra desde nodo '{inicio}'")
    print_estado(dist, prev, visitados, heap)

    paso = 0
    while heap:
        paso += 1
        d_u, u = heapq.heappop(heap)
        # Si ya procesamos una distancia mejor, ignoramos este elemento del heap
        if u in visitados:
            print(f"[Paso {paso}] Nodo {u} extraído de la cola pero ya visitado — se ignora (d={d_u})")
            if mostrar_pausa: time.sleep(pausa)
            continue

        # Confirmamos la visita del nodo u
        visitados.add(u)
        print(f"[Paso {paso}] Procesando nodo '{u}' con distancia confirmada d={d_u}")
        if mostrar_pausa: time.sleep(pausa)

        # Relajación de aristas (u -> v)
        for v, peso in graph[u]:
            print(f"   - Considerando arista {u} -> {v} (peso {peso})")
            if v in visitados:
                print(f"     * {v} ya fue visitado; no se intenta relajar.")
            else:
                alt = dist[u] + peso
                print(f"     * distancia actual a {v}: {dist[v]}; distancia por {u}: {alt}")
                if alt < dist[v]:
                    dist[v] = alt
                    prev[v] = u
                    heapq.heappush(heap, (alt, v))
                    print(f"     -> Se RELAJA: nueva distancia a {v} = {alt}; prev[{v}] = {u}")
                else:
                    print(f"     -> No se mejora la distancia a {v}")
            if mostrar_pausa: time.sleep(pausa*0.5)

        print_estado(dist, prev, visitados, heap)

    print("Algoritmo finalizado.")
    return dist, prev

def reconstruir_camino(prev, destino):
    if prev[destino] is None:
        return [destino] if destino in prev else []
    camino = []
    u = destino
    while u is not None:
        camino.append(u)
        u = prev[u]
    camino.reverse()
    return camino

def demo():
    # Ejemplo de grafo (dirigido o no; acá lo pongo como dirigido con pesos positivos)
    graph = {
        'A': [('B', 4), ('C', 2)],
        'B': [('C', 5), ('D', 10)],
        'C': [('E', 3)],
        'D': [('F', 11)],
        'E': [('D', 4)],
        'F': []
    }
    inicio = 'A'
    dist, prev = dijkstra_step_by_step(graph, inicio, mostrar_pausa=True, pausa=0.6)

    print("\nResultados finales (distancias desde A):")
    for v in sorted(dist):
        print(f"  {v}: {dist[v]}")
    # Ejemplo de reconstrucción de camino
    destino = 'F'
    camino = reconstruir_camino(prev, destino)
    if camino and dist[destino] != float('inf'):
        print(f"\nCamino más corto hasta {destino}: {' -> '.join(camino)} (costo {dist[destino]})")
    else:
        print(f"\nNo hay camino desde {inicio} hasta {destino}.")

if __name__ == "__main__":
    demo()
