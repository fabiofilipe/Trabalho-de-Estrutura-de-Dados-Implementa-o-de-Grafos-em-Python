# -*- coding: utf-8 -*-
from graph import Graph
import sys

def load_from(fileName):
    f = open(fileName, 'r')
    n = int(f.readline())

    g = Graph(n)

    l = 0
    for line in f:
        line = line.strip()
        numeros = line.split("\t")
        c = 0
        for i in numeros:
            if c == n:
                break
            g.M[l][c] = int(i)
            if int(i) != 0:
                g.L[l].append(c)
            c += 1
        l += 1

    return g

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python3 main.py <arquivo.txt> [origem destino]")
        sys.exit(1)

    arquivo = sys.argv[1]
    g = load_from(arquivo)
    g.print()

    # Número de componentes
    n = g.num_comp()
    print("Número de Componentes: " + str(n))

    # Se passados os argumentos de origem e destino, realiza BFS com caminho
    if len(sys.argv) == 4:
        origem = int(sys.argv[2])
        destino = int(sys.argv[3])
        print("\nBusca em Largura (BFS) com caminho:")
        g.bfs_path(origem, destino)

    print("\nBusca em Profundidade Iterativa (DFS):")
    g.dfs_iterative()
