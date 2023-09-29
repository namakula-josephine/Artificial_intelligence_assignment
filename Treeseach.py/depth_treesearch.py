def depth_first_search(graph, start, goal):
    stack = [(start, [])]
    
    while stack:
        node, path = stack.pop()
        if node == goal:
            return path + [node]
        
        for neighbor, _ in graph[node]:
            if neighbor not in path:
                stack.append((neighbor, path + [node]))

    return None


graph = {
    'S': [('A', 3), ('B', 1)],
    'A': [('B', 2), ('C', 2)],
    'B': [('C', 3)],
    'C': [('D', 4), ('G', 4)],
    'D': [('G', 1)],
    'G': []
}

start_node = 'S'
goal_node = 'G'

dfs_path = depth_first_search(graph, start_node, goal_node)
print("DFS Path:", dfs_path)
