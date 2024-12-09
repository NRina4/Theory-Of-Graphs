import networkx as nx
import matplotlib.pyplot as plt


def nearest_neighbor(n, edges, start_node=0):
    """ Реализует метод ближайшего соседа. """
    # Создаём матрицу смежности для хранения весов неориентированного графа
    adjacency_matrix = [[float('inf')] * n for _ in range(n)]
    for u, v, weight in edges:
        adjacency_matrix[u][v] = weight
        adjacency_matrix[v][u] = weight

    visited = set()
    path = [start_node]
    visited.add(start_node)
    total_length = 0

    current_node = start_node

    while len(visited) < n:
        # Найти ближайшего соседа
        nearest_dist = float('inf')
        next_node = -1
        for neighbor in range(n):
            if neighbor not in visited and adjacency_matrix[current_node][neighbor] < nearest_dist:
                nearest_dist = adjacency_matrix[current_node][neighbor]
                next_node = neighbor

        # Перейти к следующему узлу
        path.append(next_node)
        total_length += nearest_dist
        visited.add(next_node)
        current_node = next_node

    # Замыкаем цикл
    total_length += adjacency_matrix[current_node][start_node]
    path.append(start_node)

    return path, total_length


def visualize_nearest_neighbor(n, edges, path):
    """ Визуализация маршрута ближайшего соседа. """
    # Создаём граф
    G = nx.Graph()
    G.add_nodes_from(range(n))
    G.add_weighted_edges_from(edges)

    # Генерация позиции узлов
    pos = nx.spring_layout(G)

    # Определяем цвет рёбер: синий для маршрута, серый для остальных
    edge_colors = [
        'blue' if (u, v) in zip(path, path[1:]) or (v, u) in zip(path, path[1:]) else 'gray'
        for u, v in G.edges
    ]

    # Рисуем граф
    plt.figure(figsize=(8, 6))
    nx.draw(G, pos, with_labels=True, node_color='red', node_size=500, font_size=10, edge_color=edge_colors,
            font_weight='bold')
    nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): d['weight'] for u, v, d in G.edges(data=True)})
    plt.title("Жадный алгоритм ближайшего соседа")
    plt.show()
