# 🧠 Projeto de Grafos - Estrutura de Dados

Este projeto implementa a estrutura de **grafos** utilizando duas formas de representação:  
- Matriz de Adjacência  
- Lista de Adjacência  

Também inclui os algoritmos de:
- **Busca em Largura (BFS)** com reconstrução de caminho entre dois vértices
- **Busca em Profundidade (DFS)** reimplementada com **pilha (sem recursão)**

---

## 📁 Estrutura do Projeto

├── graph.py # Implementações do grafo, BFS, DFS recursiva e iterativa 
├── main.py # Executa o programa a partir de um arquivo .txt 
├── pcv4.txt, pvc10.txt, pvc50.txt, pvc177.txt # Exemplos de entrada do grafo  
├── Makefile # Facilita a execução via terminal 
├── README.md # Você está aqui 

---

## ⚙️ Funcionalidades

### ✅ Representações:
- **Matriz de Adjacência** (`Graph.M`)
- **Lista de Adjacência** (`Graph.L`)

### 🔍 Algoritmos:
- `bfs(source)`  
  Realiza BFS tradicional a partir de um vértice `source`.

- `bfs_path(source, target)`  
  Realiza BFS e **imprime o caminho** de `source` até `target`, se existir.

- `dfs_iterative()`  
  Realiza busca em profundidade utilizando **pilha**, **sem recursão**.

- `num_comp()`  
  Retorna o número de **componentes conexos** no grafo.

---

## 🧪 Como Executar

### ✔️ Usando o Python diretamente

```bash
python3 main.py pcv4.txt pvc10.txt pvc50.txt pvc177.txt 0 3
