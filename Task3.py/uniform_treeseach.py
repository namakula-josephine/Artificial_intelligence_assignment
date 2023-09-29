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


def uniform_cost_search(graph, start, goal):
    heap = [(0, start, [])]
    
    while heap:
        cost, node, path = heapq.heappop(heap)
        if node == goal:
            return path + [node]
        
        for neighbor, edge_cost in graph[node]:
            if neighbor not in path:
                heapq.heappush(heap, (cost + edge_cost, neighbor, path + [node]))

    return None


ucs_path = uniform_cost_search(graph, start_node, goal_node)
print("UCS Path:", ucs_path)
