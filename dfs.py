def dfs(vis, graph, node):
    vis.append(node)
    print(node, end=" ")
    for neighbour in graph[node]:
        if neighbour not in vis:
            dfs(vis, graph, neighbour)

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
    'A': ['G', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'D'],
    'D': ['A', 'E', 'F'],
    'E': ['F', 'G'],
    'F': ['C', 'B'],
    'G': ['A', 'D']
}

vis = []

start_node = input("Enter the starting node: ")
dfs(vis, graph, start_node)
