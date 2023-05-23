import graphviz


# Функция для чтения матрицы смежности из файла
def read_adj_matrix(file_path):
    with open(file_path, 'r') as f:
        adj_matrix = []
        for line in f:
            row = [int(x) for x in line.split()]
            adj_matrix.append(row)
        return adj_matrix


# Функция создания графа из матрицы смежности
def create_graph(adj_matrix):
    # Создаем новый ненаправленный граф
    dot = graphviz.Graph(strict=False)

    # Добавляем узлы в граф
    for i in range(len(adj_matrix)):
        dot.node(str(i))

    # Добавляем ребра в граф
    for i in range(len(adj_matrix)):
        for j in range(i, len(adj_matrix[i])):
            if adj_matrix[i][j] != 0:
                dot.edge(str(i), str(j), label=str(adj_matrix[i][j]))

    # Возвращаем граф
    return dot


# Функция для обхода в глубину
def dfs(graph, start_node, visited):
    visited.add(start_node)
    for neighbor in graph[start_node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# Функция для определения связанности графа
def is_connected(graph):
    visited = set()
    start_node = next(iter(graph.keys()))  # Берем первую вершину в графе
    dfs(graph, start_node, visited)
    return len(visited) == len(graph)

# Пример использования
file_path = "matrix.txt"
adj_matrix = read_adj_matrix(file_path)
graph = create_graph(adj_matrix)

# Создаем словарь, представляющий граф в виде списков смежности
adj_list = {}
for i in range(len(adj_matrix)):
    neighbors = []
    for j in range(len(adj_matrix[i])):
        if adj_matrix[i][j] != 0:
            neighbors.append(j)
    adj_list[i] = neighbors

connected = is_connected(adj_list)
print("Граф является связным" if connected else "Граф не является связным")

graph.view()
