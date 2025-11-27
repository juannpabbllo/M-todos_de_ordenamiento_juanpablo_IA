import sys

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)] 
                      for row in range(vertices)]

    def print_mst(self, parent):
        print("\n--- Árbol Parcial Mínimo Final ---")
        print("Arista \tPeso")
        total_weight = 0
        for i in range(1, self.V):
            print(f"{parent[i]} - {i} \t{self.graph[i][parent[i]]}")
            total_weight += self.graph[i][parent[i]]
        print(f"Peso Total: {total_weight}")

    def min_key(self, key, mst_set):
        # Encuentra el vértice con el valor mínimo de llave
        min_val = sys.maxsize
        min_index = -1

        for v in range(self.V):
            if key[v] < min_val and not mst_set[v]:
                min_val = key[v]
                min_index = v
        return min_index

    def prim_mst_console(self):
        key = [sys.maxsize] * self.V
        parent = [None] * self.V
        key[0] = 0
        mst_set = [False] * self.V
        parent[0] = -1

        print("Iniciando simulación paso a paso...\n")

        for cout in range(self.V):
            # Escoger el vértice de distancia mínima del conjunto no visitado
            u = self.min_key(key, mst_set)
            
            # Ponemos el vértice elegido en el set de visitados
            mst_set[u] = True
            
            if parent[u] is not None:
                print(f"Paso {cout}: Agregando nodo {u} (Conectado a {parent[u]})")
            else:
                print(f"Paso {cout}: Iniciando en nodo {u}")

            # Actualizar valor de los nodos adyacentes
            for v in range(self.V):
                if 0 < self.graph[u][v] < key[v] and not mst_set[v]:
                    key[v] = self.graph[u][v]
                    parent[v] = u
                    print(f"   -> Actualizando posible conexión: {u} - {v} con peso {self.graph[u][v]}")

        self.print_mst(parent)

# --- Ejecución ---
# Creamos un grafo de 5 nodos como ejemplo
g = Graph(5)
g.graph = [[0, 2, 0, 6, 0],
           [2, 0, 3, 8, 5],
           [0, 3, 0, 0, 7],
           [6, 8, 0, 0, 9],
           [0, 5, 7, 9, 0]]

g.prim_mst_console()