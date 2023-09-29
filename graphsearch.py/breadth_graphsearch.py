from collections import deque


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


def breadth_first_search(graph, start, goal):
    queue = deque([(start, [])])
    visited = set()
    
    while queue:
        node, path = queue.popleft()
        
        if node not in visited:
            visited.add(node)
            
            if node == goal:
                return path + [node]
            
            for neighbor, _ in graph[node]:
                if neighbor not in visited:
                    queue.append((neighbor, path + [node]))
    
    return None


bfs_path = breadth_first_search(graph, start_node, goal_node)
print("BFS Path:", bfs_path)
