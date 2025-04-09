# -*- coding: utf-8 -*-
import queue

class Graph:
    def __init__(self, n):
        self.num_vertices = n
        self.M = [[0 for _ in range(n)] for _ in range(n)]
        self.L = [[] for _ in range(n)]
    
    def print(self):
        print("Número de Vértices: " + str(self.num_vertices))
        print("Matriz de Adjacência:")
        print(self.M)
        print("Lista de Adjacência:")
        print(self.L)
    
    def num_comp(self):
        # Usa DFS recursivo para contar componentes
        pred = self.dfs()
        num = 0
        for v in range(self.num_vertices):
            if pred[v] == -1:
                num += 1
        return num
    
    def dfs(self):
        # DFS recursiva já existente
        pred = [-1 for _ in range(self.num_vertices)]
        visitados = [False for _ in range(self.num_vertices)]
        for v in range(self.num_vertices):
            if not visitados[v]:
                self.dfs_rec(v, visitados, pred)
        return pred
    
    def dfs_rec(self, v, visitados, pred):
        print("Vértice (DFS recursivo): " + str(v))
        visitados[v] = True
        for u in self.L[v]:
            if not visitados[u]:
                pred[u] = v
                self.dfs_rec(u, visitados, pred)
    
    def bfs(self, source):
        # BFS básica que guarda distância e predecessores
        visitados = [False for _ in range(self.num_vertices)]
        pred = [-1 for _ in range(self.num_vertices)]
        D = [-1 for _ in range(self.num_vertices)]
        Q = queue.Queue()
        Q.put(source)
        visitados[source] = True
        D[source] = 0
        
        while not Q.empty():
            v = Q.get()
            print("Vértice (BFS): " + str(v))
            for u in self.L[v]:
                if not visitados[u]:
                    Q.put(u)
                    visitados[u] = True
                    D[u] = D[v] + 1
                    pred[u] = v
        return D, pred
    
    def bfs_path(self, source, target):
        """
        Executa o BFS a partir de 'source' e imprime o caminho
        até 'target', reconstruindo o caminho a partir dos predecessores.
        Se não houver caminho, informa ao usuário.
        """
        D, pred = self.bfs(source)
        if D[target] == -1:
            print(f"Não há caminho entre os vértices {source} e {target}.")
            return
        
        # Reconstrução do caminho
        path = []
        at = target
        while at != -1:
            path.append(at)
            at = pred[at]
        path.reverse()
        print(f"Caminho de {source} até {target}: {path}")
    
    def dfs_iterative(self):
        """
        Implementa a busca em profundidade (DFS) de forma iterativa
        utilizando uma pilha para eliminar a recursão.
        """
        pred = [-1 for _ in range(self.num_vertices)]
        visitados = [False for _ in range(self.num_vertices)]
        
        # Percorre todos os vértices para garantir cobertura total (inclusive
        # de grafos não conexos)
        for v in range(self.num_vertices):
            if not visitados[v]:
                stack = [v]
                while stack:
                    u = stack.pop()
                    if not visitados[u]:
                        visitados[u] = True
                        print(f"Vértice visitado (DFS Iterativo): {u}")
                        # Inverte a ordem para simular a ordem de recursão
                        for w in reversed(self.L[u]):
                            if not visitados[w]:
                                pred[w] = u
                                stack.append(w)
        return pred
