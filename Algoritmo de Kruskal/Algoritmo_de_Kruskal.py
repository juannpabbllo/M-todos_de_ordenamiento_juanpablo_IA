import networkx as nx
import matplotlib.pyplot as plt
import sys

# --- Clase para manejar la lógica de Conjuntos Disjuntos (Union-Find) ---
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i]) # Compresión de ruta
        return self.parent[i]

    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)

        if root_i != root_j:
            # Unir por rango (el árbol más pequeño se une al más grande)
            if self.rank[root_i] < self.rank[root_j]:
                self.parent[root_i] = root_j
            elif self.rank[root_i] > self.rank[root_j]:
                self.parent[root_j] = root_i
            else:
                self.parent[root_j] = root_i
                self.rank[root_i] += 1
            return True # Unión exitosa
        return False # Ya estaban conectados (ciclo detectado)

# --- Simulador en Consola ---
def kruskal_console(num_nodes, edges, mode="min"):
    print(f"\n--- Iniciando Kruskal ({'MÁXIMO' if mode == 'max' else 'MÍNIMO'} Coste) ---")
    
    # 1. Ordenar aristas
    # Si es min: ascendente. Si es max: descendente (reverse=True)
    sorted_edges = sorted(edges, key=lambda item: item[2], reverse=(mode == 'max'))
    
    uf = UnionFind(num_nodes)
    mst = []
    mst_weight = 0
    
    print(f"Aristas ordenadas por peso: {sorted_edges}\n")

    step = 1
    for u, v, w in sorted_edges:
        print(f"Paso {step}: Analizando arista {u}-{v} con peso {w}...", end=" ")
        
        if uf.union(u, v):
            print(" -> ¡Aceptada! (Une dos componentes separados)")
            mst.append((u, v, w))
            mst_weight += w
        else:
            print(" -> Rechazada (Formaría un ciclo)")
        step += 1

    print("\n--- Resultado Final ---")
    print("Aristas seleccionadas:", mst)
    print(f"Costo Total: {mst_weight}")

# --- Simulador Gráfico ---
def kruskal_visual(num_nodes, edges, mode="min"):
    # Configuración Gráfica
    G = nx.Graph()
    for u, v, w in edges:
        G.add_edge(u, v, weight=w)
    
    pos = nx.spring_layout(G, seed=42) # Seed para que no se mueva
    plt.ion()
    fig, ax = plt.subplots(figsize=(10, 7))
    
    # Lógica Kruskal
    sorted_edges = sorted(edges, key=lambda item: item[2], reverse=(mode == 'max'))
    uf = UnionFind(num_nodes)
    mst_edges = []
    current_weight = 0
    
    total_steps = len(sorted_edges)
    
    for i, (u, v, w) in enumerate(sorted_edges):
        ax.clear()
        title_mode = "MÁXIMO" if mode == "max" else "MÍNIMO"
        ax.set_title(f"Kruskal {title_mode} - Analizando arista {u}-{v} (Peso {w})\nCosto Acumulado: {current_weight}")
        
        # Dibujar grafo base (gris)
        nx.draw_networkx_edges(G, pos, alpha=0.2, edge_color='gray', width=1)
        nx.draw_networkx_nodes(G, pos, node_color='lightblue', node_size=500)
        nx.draw_networkx_labels(G, pos)
        edge_labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
        
        # Dibujar MST acumulado (Verde)
        if mst_edges:
            nx.draw_networkx_edges(G, pos, edgelist=mst_edges, width=4, edge_color='green')
        
        # Dibujar arista actual que se está evaluando (Naranja)
        nx.draw_networkx_edges(G, pos, edgelist=[(u, v)], width=4, edge_color='orange')
        
        plt.draw()
        plt.pause(1.5) # Pausa para ver la animación
        
        # Decisión
        if uf.union(u, v):
            mst_edges.append((u, v))
            current_weight += w
            # Mostrar brevemente en verde que fue aceptada
            nx.draw_networkx_edges(G, pos, edgelist=[(u, v)], width=5, edge_color='blue')
            plt.pause(0.5)
        else:
            # Mostrar brevemente en rojo que fue rechazada
            nx.draw_networkx_edges(G, pos, edgelist=[(u, v)], width=5, edge_color='red', style='dashed')
            plt.pause(0.5)

    # Final
    ax.clear()
    ax.set_title(f"¡Kruskal Finalizado! Costo Total: {current_weight}")
    nx.draw_networkx_edges(G, pos, alpha=0.1, edge_color='gray')
    nx.draw_networkx_edges(G, pos, edgelist=mst_edges, width=4, edge_color='green')
    nx.draw_networkx_nodes(G, pos, node_color='lightgreen', node_size=600)
    nx.draw_networkx_labels(G, pos)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    
    plt.ioff()
    plt.show()

# --- Configuración del Grafo y Menú ---
if __name__ == "__main__":
    # Nodos: 0, 1, 2, 3, 4, 5
    # Formato: (nodo_origen, nodo_destino, peso)
    mis_aristas = [
        (0, 1, 4), (0, 2, 4),
        (1, 2, 2), (1, 0, 4), (2, 3, 3), (2, 5, 2), (2, 4, 4),
        (3, 4, 3), (5, 4, 3)
    ]
    num_nodos = 6
    
    print("Simulador de Kruskal")
    print("1. Mínimo Coste (Consola)")
    print("2. Mínimo Coste (Gráfico)")
    print("3. Máximo Coste (Consola)")
    print("4. Máximo Coste (Gráfico)")
    
    opcion = input("Elige una opción (1-4): ")
    
    if opcion == '1':
        kruskal_console(num_nodos, mis_aristas, mode="min")
    elif opcion == '2':
        kruskal_visual(num_nodos, mis_aristas, mode="min")
    elif opcion == '3':
        kruskal_console(num_nodos, mis_aristas, mode="max")
    elif opcion == '4':
        kruskal_visual(num_nodos, mis_aristas, mode="max")
    else:
        print("Opción no válida")