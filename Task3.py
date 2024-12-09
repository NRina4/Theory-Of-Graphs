import math
import random
import networkx as nx
import matplotlib.pyplot as plt


def turan_graph(n, r):
    # Вычисляем размеры долей
    l1 = math.ceil(n / r)
    l2 = math.floor(n / r)

    # Определяем количество долей размера l1 и l2
    k1 = n % r
    k2 = r - k1

    # Распределяем вершины по долям
    partitions = []
    vertex = 0
    for _ in range(k1):
        partitions.append(list(range(vertex, vertex + l1)))
        vertex += l1
    for _ in range(k2):
        partitions.append(list(range(vertex, vertex + l2)))
        vertex += l2

    # Создаем граф и добавляем ребра между вершинами из разных долей
    graph = nx.Graph()
    for i in range(len(partitions)):
        for j in range(i + 1, len(partitions)):
            for u in partitions[i]:
                for v in partitions[j]:
                    graph.add_edge(u, v)

    return graph


def generate_random_graph(n, density):
    if density < 0 or density > 1:
        raise ValueError("Плотность должна быть между 0 и 1.")

    # Создаём пустой граф с n вершинами
    graph = nx.Graph()
    graph.add_nodes_from(range(n))

    # Максимальное число рёбер
    max_edges = n * (n - 1) // 2
    target_edges = round(density * max_edges)

    # Список всех возможных рёбер
    possible_edges = [(i, j) for i in range(n) for j in range(i + 1, n)]
    random.shuffle(possible_edges)

    # Добавляем случайные рёбра, пока не достигнем целевого числа
    for edge in possible_edges[:target_edges]:
        graph.add_edge(*edge)

    return graph


def visualize_graph(graph, title):
    nx.draw(graph, with_labels=True, node_size=700, node_color="lightblue", font_size=12, font_weight="bold")
    plt.title(title)
    plt.show()

