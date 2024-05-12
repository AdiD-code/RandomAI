from aco_routing import ACO
import networkx as nx

# Provided graph
G = nx.DiGraph()

G.add_edge("A", "B", cost=2)
G.add_edge("B", "C", cost=2)
G.add_edge("A", "H", cost=2)
G.add_edge("H", "G", cost=2)
G.add_edge("C", "F", cost=1)
G.add_edge("F", "G", cost=1)
G.add_edge("G", "F", cost=1)
G.add_edge("F", "C", cost=1)
G.add_edge("C", "D", cost=10)
G.add_edge("E", "D", cost=2)
G.add_edge("G", "E", cost=2)

# Uncomment the below section to create the graph interactively
"""
def create_graph_from_input():
    G = nx.DiGraph()
    
    num_edges = int(input("Enter the number of edges: "))
    print("Enter edges and their costs (e.g., A B 2):")
    for _ in range(num_edges):
        src, dest, cost = input().split()
        cost = int(cost)
        G.add_edge(src, dest, cost=cost)
    
    return G

G = create_graph_from_input()
"""


aco = ACO(G, ant_max_steps=100, num_iterations=100, ant_random_spawn=True)

source = input("Enter the source node: ")
destination = input("Enter the destination node: ")

num_ants = int(input("Enter the number of ants: "))

aco_path, aco_cost = aco.find_shortest_path(
    source=source,
    destination=destination,
    num_ants=num_ants,
)

print("ACO Path: ", end="")
for i, node in enumerate(aco_path):
    if i != 0:
        print(" -> ", end="")
    print(node, end="")

print("\nACO Cost:", aco_cost)