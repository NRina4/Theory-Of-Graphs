from itertools import combinations
import networkx as nx
import matplotlib.pyplot as plt


def is_k_regular(graph, subset, k):
    """
    Проверяет, является ли подграф, порожденный subset, k-правильным.
    """
    # Подсчет степени каждой вершины в подграфе
    degree = {v: 0 for v in subset}
    for u, v in graph:
        if u in subset and v in subset:  # Ребро внутри подграфа
            degree[u] += 1
            degree[v] += 1
    # Проверяем, равна ли степень каждой вершины k
    return all(deg == k for deg in degree.values())


def find_regular_subgraphs(n, edges):
    """
    Находит все правильные подграфы для всех возможных степеней k.
    """
    vertices = range(n)
    regular_subgraphs = {}  # Словарь для хранения подграфов по степеням k
    max_degree = n - 1  # Максимальная возможная степень вершины

    # Перебираем все подмножества вершин
    for r in range(1, n + 1):  # Минимальный размер подграфа — 1 вершина
        for subset in combinations(vertices, r):
            subset_set = set(subset)
            # Проверяем для всех возможных k
            for k in range(max_degree + 1):
                if is_k_regular(edges, subset_set, k):
                    if k not in regular_subgraphs:
                        regular_subgraphs[k] = []
                    regular_subgraphs[k].append(subset_set)

    return regular_subgraphs


def visualize_graph(edges, subset, title, all_nodes):
    """
    Визуализация подграфа.

    :param edges: список рёбер основного графа.
    :param subset: множество вершин текущего подграфа.
    :param title: заголовок для графика.
    :param all_nodes: все вершины основного графа.
    """
    G = nx.Graph()
    G.add_edges_from(edges)  # Добавляем рёбра
    G.add_nodes_from(all_nodes)  # Добавляем все вершины графа

    pos = nx.spring_layout(G)  # Расположение вершин для визуализации

    # Подграф: выделяем вершины и рёбра
    sub_edges = [(u, v) for u, v in edges if u in subset and v in subset]
    sub_nodes = list(subset)

    plt.figure(figsize=(6, 6))
    # Рисуем весь граф серым
    nx.draw(G, pos, with_labels=True, node_color='lightgray', edge_color='gray', node_size=500, font_size=10)
    # Рисуем вершины и рёбра подграфа
    nx.draw_networkx_nodes(G, pos, nodelist=sub_nodes, node_color='orange', node_size=600)
    nx.draw_networkx_edges(G, pos, edgelist=sub_edges, edge_color='red', width=2)
    plt.title(title)
    plt.show()


if __name__ == '__main__':
    # Входные данные
    n = 5
    edges = [(0, 1), (0, 2), (0, 3), (0, 4), (1, 2), (1, 3), (2, 3), (3, 4)]

    # Поиск регулярных подграфов
    regular_subgraphs = find_regular_subgraphs(n, edges)
    # Все вершины основного графа
    all_nodes = range(n)
    # Вывод и визуализация
    for k, subgraphs in regular_subgraphs.items():
        print(f"Регулярные подграфы для k = {k}:")
        for i, subgraph in enumerate(subgraphs, 1):
            print(subgraph)
            title = f"Регулярный подграф (k={k}, Подграф #{i})"
            visualize_graph(edges, subgraph, title, all_nodes)
