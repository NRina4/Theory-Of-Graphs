import math
import itertools
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque


# Функция для нахождения всех правильных подграфов
def find_induced_subgraphs(n, edges):
    graph = nx.Graph()
    graph.add_nodes_from(range(n))
    graph.add_edges_from(edges)

    nodes = list(graph.nodes())
    all_subgraphs = []

    for r in range(1, len(nodes) + 1):
        for subset in itertools.combinations(nodes, r):
            induced_subgraph = graph.subgraph(subset).copy()
            all_subgraphs.append(induced_subgraph)

    return all_subgraphs


# Визуализация всех правильных подграфов
def visualize_subgraphs(subgraphs):
    num_subgraphs = len(subgraphs)
    grid_size = math.ceil(math.sqrt(num_subgraphs))
    plt.figure(figsize=(grid_size * 4, grid_size * 4))

    for i, item in enumerate(subgraphs, start=1):
        plt.subplot(grid_size, grid_size, i)
        if isinstance(subgraphs[0], tuple):
            graph, title = item
        else:
            graph, title = item, f"Подграф {i}"
        nx.draw(graph, with_labels=True, node_color='green', node_size=400, font_size=10, font_color='white')
        plt.title(title)

    plt.tight_layout()
    plt.show()


# ---------------------------------------------------------------------------------------------------------------------#

# Функция для создания графа в виде списка смежности
def create_graph(n, edges):
    graph = {i: [] for i in range(n)}
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    return graph


# Функция дизъюнктного объединения графов
def disjoint_union(graph1, graph2):
    n1 = len(graph1)
    result = {**graph1}  # Копируем первый граф
    for u, neighbors in graph2.items():
        result[u + n1] = [v + n1 for v in neighbors]  # Смещаем индексы второго графа
    return result


# Функция соединение графов
def join(graph1, graph2):
    n1 = len(graph1)  # Количество вершин в первом графе
    n2 = len(graph2)  # Количество вершин во втором графе

    # Создаём копию graph1
    result = {u: neighbors[:] for u, neighbors in graph1.items()}
    # Добавляем вершины и рёбра из graph2 с перенумерацией
    for u, neighbors in graph2.items():
        result[u + n1] = [v + n1 for v in neighbors]
    # Добавляем рёбра между вершинами graph1 и graph2
    for u in graph1:
        for v in range(n1, n1 + n2):  # Новые вершины из graph2
            result[u].append(v)
            result[v].append(u)
    return result


# Функция пересечения графов
def intersection(graph1, graph2):
    result = {i: [v for v in graph1.get(i, []) if v in graph2.get(i, [])] for i in set(graph1) & set(graph2)}
    return {k: v for k, v in result.items() if v}


# Функция для дополнения графа
def complement(n, graph):
    result = {i: [] for i in range(n)}
    for u in range(n):
        for v in range(n):
            if u != v and v not in graph.get(u, []):
                result[u].append(v)
    return result


# Функция удаления выбранных вершин
def remove_vertices(graph, vertices):
    result = {
        k: [v for v in adj if v not in vertices]  # Удаляем рёбра, ведущие к удаляемым вершинам
        for k, adj in graph.items()  # Обходим все вершины графа и их соседей
        if k not in vertices  # Исключаем удаляемые вершины
    }
    return result


# Функция для перевода списка смежности в граф NetworkX
def adjacency_to_nx(graph):
    G = nx.Graph()
    # Добавляем все вершины (включая изолированные)
    G.add_nodes_from(graph.keys())
    # Добавляем рёбра
    for node, neighbors in graph.items():
        for neighbor in neighbors:
            G.add_edge(node, neighbor)
    return G


# ----------------------------------------------------------------------------------------------------------------------#

def graph_traversal(graph, start_vertex, method="bfs"):
    visited = {v: 0 for v in graph}  # Словарь для отметки посещённых вершин
    traversal = []  # Результат обхода
    match method:
        case "bfs":
            structure = deque()  # Очередь для BFS
        case "dfs":
            structure = []  # Стек для DFS
        case _:
            raise ValueError("Метод должен быть 'bfs' или 'dfs'.")

    # Начальная вершина
    structure.append(start_vertex)
    visited[start_vertex] = 1

    while structure:
        # Извлечение вершины
        match method:
            case "bfs":
                current_vertex = structure.popleft()
            case _:
                current_vertex = structure.pop()

        traversal.append(current_vertex)  # Добавление вершины в результат

        # Обработка соседей
        for neighbor in graph[current_vertex]:
            if not visited[neighbor]:
                structure.append(neighbor)
                visited[neighbor] = 1

    return traversal
