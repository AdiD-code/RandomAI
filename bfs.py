def bfs(vis, graph, node):
    vis.append(node)
    queue.append(node)
   
    while queue:
        s = queue.pop(0)
        print(s, end=" ")
     
        for neighbour in graph[s]:
            if neighbour not in vis:
                vis.append(neighbour)
                queue.append(neighbour)

# Taking graph as user input
"""
graph = {}
nodes = int(input("Enter the number of nodes: "))

for i in range(nodes):
    node = input(f"Enter the node {i+1}: ")
    connections = input(f"Enter the connections for node {node}: ").split(',')
    graph[node] = connections
    """

graph = {
 'A' : ['G', 'C'],
 'B' : ['D', 'E'],
 'C' : ['F', 'D'],
 'D' : ['A', 'E', 'F'],
 'E' : ['F', 'G'],
 'F' : ['C', 'B'],
 'G' : ['A', 'D']
}

vis = []
queue = []

start_node = input("Enter the starting node: ")
bfs(vis, graph, start_node)
