import heapq


graph = {
    'S': {('A', 3), ('B', 1)},
    'A': {('B', 2), ('C', 2)},
    'B': {('C', 3)},
    'C': {('D', 4), ('G', 4)},
    'D': {('G', 1)},
    'G': set()
}


start_node = 'S'
goal_node = 'G'


heuristics = {
    'S': 7,
    'A': 5,
    'B': 7,
    'C': 4,
    'D': 1,
    'G': 0
}


def astar_search(graph, start, goal, heuristics):
    heap = [(heuristics[start], 0, start, [])]
    visited = set()
    
    while heap:
        _, cost, node, path = heapq.heappop(heap)
        
        if node not in visited:
            visited.add(node)
            
            if node == goal:
                return path + [node]
            
            for neighbor, edge_cost in graph[node]:
                if neighbor not in visited:
                    heapq.heappush(heap, (cost + edge_cost + heuristics[neighbor], cost + edge_cost, neighbor, path + [node]))
    
    return None


astar_path = astar_search(graph, start_node, goal_node, heuristics)
print("A* Search Path:", astar_path)
