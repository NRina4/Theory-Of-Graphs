from itertools import combinations

import networkx as nx
import matplotlib.pyplot as plt


def is_independent_set(edges, subset):
    """ Проверяет, является ли подмножество вершин независимым в графе. """
    for i in range(len(subset)):
        for j in range(i + 1, len(subset)):
            if (subset[i], subset[j]) in edges or (subset[j], subset[i]) in edges:
                return False
    return True


def find_max_independent_set_bruteforce(n, edges):
    """ Алгоритм полного перебора для нахождения наибольшего независимого множества вершин. """
    max_independent_set = set()
    vertices = set(range(n))

    # Перебираем все подмножества вершин
    for r in range(len(max_independent_set) + 1, len(vertices) + 1):
        for subset in combinations(vertices, r):
            if is_independent_set(edges, subset):
                max_independent_set = set(subset)

    return max_independent_set


def find_max_independent_set_backtracking(n, edges, S=None, T=None):
    """ Алгоритм поиска с возвратом для нахождения наибольшего независимого множества вершин. """
    # Инициализация на первом вызове
    if S is None and T is None:
        S = set()
        T = set(range(n))

    # Если T пусто, возвращаем S как результат
    if not T:
        return S

    best_result = S.copy()  # Текущее лучшее множество

    for v in list(T):  # Преобразуем T в список, чтобы можно было итерировать
        # Формируем новое множество оставшихся вершин (без v и её соседей)
        new_T = T - {v} - {u for u in T if (u, v) in edges or (v, u) in edges}

        # Рекурсивно вызываем для нового S и T
        candidate_result = find_max_independent_set_backtracking(n, edges, S | {v}, new_T)

        # Обновляем лучший результат, если нашли большее множество
        if len(candidate_result) > len(best_result):
            best_result = candidate_result

    return best_result


def visualize_graph(n, edges, independent_set):
    """ Визуализирует граф с выделением независимого множества. """
    G = nx.Graph()
    G.add_nodes_from(range(n))
    G.add_edges_from(edges)

    node_colors = ["red" if node in independent_set else "lightblue" for node in G.nodes]

    pos = nx.spring_layout(G)
    nx.draw(
        G=G,
        pos=pos,
        with_labels=True,
        node_color=node_colors,
        node_size=500,
        font_size=10,
        font_color="black",
        edge_color="gray",
    )
    plt.title("Граф с выделенным максимальным независимым множеством")
    plt.show()
