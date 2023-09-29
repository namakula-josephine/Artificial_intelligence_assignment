
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


def greedy_search(graph, start, goal, heuristics):
    queue = [(heuristics[start], start, [])]
    visited = set()
    
    while queue:
        _, node, path = min(queue)
        queue.remove((heuristics[node], node, path))
        
        if node not in visited:
            visited.add(node)
            
            if node == goal:
                return path + [node]
            
            for neighbor, _ in graph[node]:
                if neighbor not in visited:
                    queue.append((heuristics[neighbor], neighbor, path + [node]))
    
    return None


greedy_path = greedy_search(graph, start_node, goal_node, heuristics)
print("Greedy Search Path:", greedy_path)
