import math

class Node:

    def __init__(self, value=None, children=[]):
        self.value = value
        self.children = children

def minimax(node, depth, maximizing_player):    
    if depth == 0 or len(node.children) == 0:
        return node.value

    if maximizing_player:
        max_eval = -math.inf
        for child in node.children:
            eval = minimax(child, depth - 1, False)
            max_eval = max(max_eval, eval)

        return max_eval
    
    else:
        min_eval = math.inf
        for child in node.children:
            eval = minimax(child, depth - 1, True)
            min_eval = min(min_eval, eval)

        return min_eval

# Example tree
tree =  Node(value=None, children=[
    Node(value=None, children=[
        Node(value=3),
        Node(value=12),
        Node(value=8)
    ]),

    Node(value=None, children=[
        Node(value=2),
        Node(value=4),
        Node(value=6)
    ]),

    Node(value=None, children=[
        Node(value=14),
        Node(value=5),
        Node(value=7)
    ])
])

result = minimax(tree, 2, True)
print("The optimal value is:", result)

# Uncomment the below section to take graph as user input
"""
def create_tree_from_input():
    num_nodes = int(input("Enter the number of nodes in the tree: "))
    nodes = [Node() for _ in range(num_nodes)]
    
    for i, node in enumerate(nodes):
        print(f"Enter children for node {i}:")
        children_indices = list(map(int, input().split()))
        node.children = [nodes[child_index] for child_index in children_indices]
        
        value = int(input(f"Enter value for node {i}: "))
        node.value = value
        
    return nodes[0]  # Return the root node

# Uncomment the below lines to use user input for creating the tree
# tree = create_tree_from_input()
# result = minimax(tree, 2, True)
# print("The optimal value is:", result)
"""
