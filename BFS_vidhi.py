from collections import deque

def build_graph():
    num_vertices = int(input("Enter the number of vertices: "))
    graph = {i: [] for i in range(num_vertices)}

    print("Enter edges (format: u v). Type 'done' to finish:")
    while True:
        edge = input("Edge: ")
        if edge.lower() == "done":
            break
        try:
            u, v = map(int, edge.split())
            if u < 0 or v < 0 or u >= num_vertices or v >= num_vertices:
                print("Invalid vertex number. Try again.")
                continue
            graph[u].append(v)
            graph[v].append(u)  # Remove this line if the graph is directed
        except:
            print("Invalid input. Please enter in format: u v")
    
    return graph, num_vertices

def adjacency_matrix(graph, num_vertices):
    matrix = [[0] * num_vertices for _ in range(num_vertices)]
    for u in graph:
        for v in graph[u]:
            matrix[u][v] = 1
    return matrix

def bfs(graph, start):
    visited = set()
    queue = deque()
    order = []

    queue.append(start)
    visited.add(start)

    print("\nBFS Traversal:")
    while queue:
        vertex = queue.popleft()  
        print(f"Visited: {vertex}")
        order.append(vertex)

        for neighbor in graph[vertex]:
            if neighbor not in visited:
                queue.append(neighbor)  
                visited.add(neighbor)
    
    return order

def print_adjacency_matrix(matrix):
    print("\nAdjacency Matrix:")
    for row in matrix:
        print(" ".join(map(str, row)))

if __name__ == "__main__":
    graph, num_vertices = build_graph()
    matrix = adjacency_matrix(graph, num_vertices)

    print_adjacency_matrix(matrix)

    start_vertex = int(input(f"\nEnter starting vertex (0 to {num_vertices - 1}): "))
    if start_vertex < 0 or start_vertex >= num_vertices:
        print("Invalid start vertex.")
    else:
        traversal_order = bfs(graph, start_vertex)
        print("\nFinal BFS Order:", traversal_order)
