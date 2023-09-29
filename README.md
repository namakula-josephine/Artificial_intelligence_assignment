# Artificial_intelligence_assignment
class work
Task 1.

a. Depth-First Search
Depth-First Search (DFS) explores a graph or tree by going as deep as possible along each branch before backtracking.
Tree Search: DFS starts at the root (or any arbitrary node) of a tree and explores as far as possible along each branch before backtracking.
Graph Search: In a graph, DFS starts at any node and explores as far as possible along each branch before backtracking. The main difference from tree search is that we have to keep track of the nodes we've visited to avoid cycles or repeated states.

b. Breadth-First Search
Breadth-First Search (BFS) explores all the neighbors at the present depth before moving on to nodes at the next depth level.
Tree Search: In a tree, BFS starts at the root (or any arbitrary node) and explores the neighbor nodes at the current depth level before moving on to nodes at the next depth level.
Graph Search: The operation of BFS in graph search is similar to tree search. The main difference is that we keep track of the nodes we've visited to avoid cycles and repeated states

c. Uniform Cost Search
Uniform Cost Search (UCS) is a tree search algorithm used for traversing or searching a weighted tree or graph. It prioritizes nodes with the lowest total cost.
Tree Search and Graph Search: The operation of UCS is the same for both tree and graph. It starts with the root (or any arbitrary node) and expands the node with the lowest path cost, as determined by a priority queue. For graphs, we need to avoid revisiting already processed nodes.



d. Greedy Search
Greedy Search algorithm follows the problem-solving heuristic of making the locally optimal choice at each stage with the hope that these local solutions will lead to a global optimum.
Tree Search and Graph Search: In both cases, the greedy search algorithm selects the path that appears best at the moment. It uses a heuristic to estimate the cost of getting to the goal from each node and selects the path with the minimum heuristic cost. For graphs, we maintain a closed list of visited nodes to avoid cycles.

e. A* Search
A Search* algorithm is a combination of the best features of UCS and Greedy Search. It uses a heuristic to estimate the cost to get to the goal (like Greedy Search) and also considers the cost to get to the current state (like UCS).
Tree Search and Graph Search: A* Search starts at the root (or any arbitrary node) and selects the node with the lowest combined cost and heuristic estimate to expand next. For graphs, we maintain a closed list of visited nodes to avoid cycles.
 
