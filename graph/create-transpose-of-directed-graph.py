
"""
For your reference:
class GraphNode:
    def __init__(self, value):
        self.value = value
        self.neighbors = []
"""
from collections import defaultdict
class GraphNode:
    def __init__(self, value):
        self.value = value
        self.neighbors = []

def create_transpose(node):
    """
    Args:
     node(GraphNode_int32)
    Returns:
     GraphNode_int32
    """
    # Write your code here.
    visited = set()
    def dfs(node):
        for neighbour in node.neighbors:
            if (node, neighbour) not in visited:
                
                visited.add((node, neighbour))
                #   Remove the node->neighbour connection from node.neighbors
                node.neighbors.remove(neighbour)
                #   Add the neighbour->node connection for neighbour.neighbors
                neighbour.neighbors.append(node)
                visited.add((neighbour, node))

                dfs(neighbour)

    dfs(node)
    return node


if __name__ == "__main__":
    node = GraphNode(1)
    node_2 = GraphNode(2)
    node_3 = GraphNode(3)
    node.neighbors = [node_2]
    node_2.neighbors = [node_3]
    node_3.neighbors = [node]
    # create_transpose(node)

    node_0 = GraphNode(0)
    node_1 = GraphNode(1)
    node_2 = GraphNode(2)
    node_3 = GraphNode(3)
    node_4 = GraphNode(4)

    node_0.neighbors = [node_3, node_2]
    node_1.neighbors = [node_0]
    node_2.neighbors = [node_1]
    node_3.neighbors = [node_4]
    node_4.neighbors = [node_2]
    # create_transpose(node_0)

    node_1 = GraphNode(1)
    node_2 = GraphNode(2)

    node_1.neighbors = [node_2]
    node_2.neighbors = [node_1]
    create_transpose(node_1)
