# NAMAKULA JOSEPHINE
# 2200703590
# 22/U/3590/EVE


import heapq

graph = {
    'S': {'neighbors': {'A': 3, 'B': 1}, 'heuristic': 7},
    'A': {'neighbors': {'B': 2, 'C': 2}, 'heuristic': 5},
    'B': {'neighbors': {'C': 3}, 'heuristic': 7},
    'C': {'neighbors': {'D': 4, 'G': 4}, 'heuristic': 4},
    'D': {'neighbors': {'G': 1}, 'heuristic': 1},
    'G': {'neighbors': {}, 'heuristic': 0}
}

# Depth-First Search (Tree Search)
def depth_first_search_tree(graph, start, goal):
    stack = [(start, [])]
    visited = set()

    while stack:
        node, path = stack.pop()
        if node == goal:
            path.append(node)  # Include the goal state 'G' in the path
            return "Depth-First Search (Tree Search):", path
        if node not in visited:
            visited.add(node)
            neighbors = [neighbor for neighbor in graph[node]['neighbors']]
            stack.extend((neighbor, path + [node]) for neighbor in reversed(neighbors) if neighbor not in visited)

# Breadth-First Search (Tree Search)
def breadth_first_search_tree(graph, start, goal):
    queue = [(start, [])]
    visited = set()

    while queue:
        node, path = queue.pop(0)
        if node == goal:
            path.append(node)  # Include the goal state 'G' in the path
            return "Breadth-First Search (Tree Search):", path
        if node not in visited:
            visited.add(node)
            neighbors = [neighbor for neighbor in graph[node]['neighbors']]
            queue.extend((neighbor, path + [node]) for neighbor in neighbors if neighbor not in visited)

# Uniform Cost Search (Tree Search)
def uniform_cost_search_tree(graph, start, goal):
    priority_queue = [(0, start, [])]
    visited = set()

    while priority_queue:
        cost, node, path = heapq.heappop(priority_queue)
        if node == goal:
            path.append(node)  # Include the goal state 'G' in the path
            return "Uniform Cost Search (Tree Search):", path
        if node not in visited:
            visited.add(node)
            neighbors = [(neighbor, cost + graph[node]['neighbors'][neighbor]) for neighbor in graph[node]['neighbors']]
            for neighbor, new_cost in neighbors:
                heapq.heappush(priority_queue, (new_cost, neighbor, path + [node]))

# Greedy Search (Tree Search)
def greedy_search_tree(graph, start, goal):
    priority_queue = [(graph[start]['heuristic'], start, [])]
    visited = set()

    while priority_queue:
        _, node, path = heapq.heappop(priority_queue)
        if node == goal:
            path.append(node)  # Include the goal state 'G' in the path
            return "Greedy Search (Tree Search):", path
        if node not in visited:
            visited.add(node)
            neighbors = [neighbor for neighbor in graph[node]['neighbors']]
            priority_queue.extend((graph[neighbor]['heuristic'], neighbor, path + [node]) for neighbor in neighbors if neighbor not in visited)

# A* Search (Tree Search)
def a_star_search_tree(graph, start, goal):
    priority_queue = [(graph[start]['heuristic'], 0, start, [])]
    visited = set()

    while priority_queue:
        _, cost_so_far, node, path = heapq.heappop(priority_queue)
        if node == goal:
            path.append(node)  # Include the goal state 'G' in the path
            return "A* Search (Tree Search):", path
        if node not in visited:
            visited.add(node)
            neighbors = [(neighbor, cost_so_far + graph[node]['neighbors'][neighbor]) for neighbor in graph[node]['neighbors']]
            for neighbor, new_cost in neighbors:
                heapq.heappush(priority_queue, (new_cost + graph[neighbor]['heuristic'], new_cost, neighbor, path + [node]))

# Test the search algorithms for Tree Search
goal_state = 'G'
print(*depth_first_search_tree(graph, 'S', goal_state), "\n")
print(*breadth_first_search_tree(graph, 'S', goal_state), "\n")
print(*uniform_cost_search_tree(graph, 'S', goal_state), "\n")
print(*greedy_search_tree(graph, 'S', goal_state), "\n")
print(*a_star_search_tree(graph, 'S', goal_state), "\n\n\n")


# Depth-First Search (Graph Search)
def depth_first_search_graph(graph, start, goal):
    stack = [(start, [])]
    visited = set()

    while stack:
        node, path = stack.pop()
        if node == goal:
            path.append(node)  # Include the goal state 'G' in the path
            return "Depth-First Search (Graph Search):", path
        if node not in visited:
            visited.add(node)
            neighbors = [neighbor for neighbor in graph[node]['neighbors']]
            stack.extend((neighbor, path + [node]) for neighbor in reversed(neighbors) if neighbor not in visited)

    # If the goal is not found, you can return an appropriate message
    return "Depth-First Search (Graph Search): Goal not found"

# Breadth-First Search (Graph Search)
def breadth_first_search_graph(graph, start, goal):
    queue = [(start, [])]
    visited = set()

    while queue:
        node, path = queue.pop(0)
        if node == goal:
            path.append(node)  # Include the goal state 'G' in the path
            return "Breadth-First Search (Graph Search):", path
        if node not in visited:
            visited.add(node)
            neighbors = [neighbor for neighbor in graph[node]['neighbors']]
            queue.extend((neighbor, path + [node]) for neighbor in neighbors if neighbor not in visited)

    # If the goal is not found, you can return an appropriate message
    return "Breadth-First Search (Graph Search): Goal not found"

# Uniform Cost Search (Graph Search)
def uniform_cost_search_graph(graph, start, goal):
    priority_queue = [(0, start, [])]
    visited = set()

    while priority_queue:
        cost, node, path = heapq.heappop(priority_queue)
        if node == goal:
            path.append(node)  # Include the goal state 'G' in the path
            return "Uniform Cost Search (Graph Search):", path
        if node not in visited:
            visited.add(node)
            neighbors = [(neighbor, cost + graph[node]['neighbors'][neighbor]) for neighbor in graph[node]['neighbors']]
            for neighbor, new_cost in neighbors:
                heapq.heappush(priority_queue, (new_cost, neighbor, path + [node]))

    # If the goal is not found, you can return an appropriate message
    return "Uniform Cost Search (Graph Search): Goal not found"

# Greedy Search (Graph Search)
def greedy_search_graph(graph, start, goal):
    priority_queue = [(graph[start]['heuristic'], start, [])]
    visited = set()

    while priority_queue:
        _, node, path = heapq.heappop(priority_queue)
        if node == goal:
            path.append(node)  # Include the goal state 'G' in the path
            return "Greedy Search (Graph Search):", path
        if node not in visited:
            visited.add(node)
            neighbors = [neighbor for neighbor in graph[node]['neighbors']]
            priority_queue.extend((graph[neighbor]['heuristic'], neighbor, path + [node]) for neighbor in neighbors if neighbor not in visited)

    # If the goal is not found, you can return an appropriate message
    return "Greedy Search (Graph Search): Goal not found"

# A* Search (Graph Search)
def a_star_search_graph(graph, start, goal):
    priority_queue = [(graph[start]['heuristic'], 0, start, [])]
    visited = set()

    while priority_queue:
        _, cost_so_far, node, path = heapq.heappop(priority_queue)
        if node == goal:
            path.append(node)  # Include the goal state 'G' in the path
            return "A* Search (Graph Search):", path
        if node not in visited:
            visited.add(node)
            neighbors = [(neighbor, cost_so_far + graph[node]['neighbors'][neighbor]) for neighbor in graph[node]['neighbors']]
            for neighbor, new_cost in neighbors:
                heapq.heappush(priority_queue, (new_cost + graph[neighbor]['heuristic'], new_cost, neighbor, path + [node]))

    # If the goal is not found, you can return an appropriate message
    return "A* Search (Graph Search): Goal not found"

# Test the search algorithms for Graph Search
goal_state = 'G'
print(*depth_first_search_graph(graph, 'S', goal_state), "\n")
print(*breadth_first_search_graph(graph, 'S', goal_state), "\n")
print(*uniform_cost_search_graph(graph, 'S', goal_state), "\n")
print(*greedy_search_graph(graph, 'S', goal_state), "\n")
print(*a_star_search_graph(graph, 'S', goal_state), "\n")
