from itertools import permutations

def tsp(graph, start):
    vertices = list(graph.keys())
    vertices.remove(start)
    min_path = float('inf')
    best_route = None
    
    for perm in permutations(vertices):
        current_path = 0
        k = start
        for j in perm:
            current_path += graph[k][j]
            k = j
        current_path += graph[k][start]
        
        if current_path < min_path:
            min_path = current_path
            best_route = (start,) + perm + (start,)
    
    print("Minimum cost: ", min_path)
    print("Best Route: ", best_route)

graph = {
    'A': {'B': 10, 'C': 15, 'D': 20},
    'B': {'A': 10, 'C': 35, 'D': 25},
    'C': {'A': 15, 'B': 35, 'D': 30},
    'D': {'A': 20, 'B': 25, 'C': 30}
}

tsp(graph, 'A')
