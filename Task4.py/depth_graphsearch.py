
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


def depth_first_search(graph, start, goal):
    stack = [(start, [])]
    visited = set()
    
    while stack:
        node, path = stack.pop()
        
        if node not in visited:
            visited.add(node)
            
            if node == goal:
                return path + [node]
            
            for neighbor, _ in graph[node]:
                if neighbor not in visited:
                    stack.append((neighbor, path + [node]))
    
    return None


dfs_path = depth_first_search(graph, start_node, goal_node)
print("DFS Path:", dfs_path)
