def dfs(graph, node, max_depth):
    stack = [(node, 0)]
    vis = []

    while stack:
        current_node, depth = stack.pop()
        if current_node not in vis:
            print(current_node, end=" ")  # Print the current node
            vis.append(current_node)
            if depth < max_depth:
                for neighbour in graph[current_node]:
                    stack.append((neighbour, depth + 1))

def iddfs(graph, start_node):
    depth = 0
    while True:
        print(f"\nDepth {depth}: ", end="")
        dfs(graph, start_node, depth)
        depth += 1
        if depth > len(graph):  # Maximum depth reached
            break


# Taking graph as user input
"""
graph = {}
nodes = int(input("Enter the number of nodes: "))

for i in range(nodes):
    node = input(f"Enter the node {i+1}: ")
    connections = input(f"Enter the connections for node {node}: ").split(',')
    graph[node] = connections
"""

# Graph provided
graph = {
    'A': ['B', 'D'],
    'B': ['C', 'E'],
    'C': [],
    'D': ['E', 'F'],
    'E': ['G'],
    'F': [],
    'G': []
}

vis = []

start_node = input("Enter the starting node: ")
iddfs(graph, start_node)


