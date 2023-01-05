from collections import defaultdict

# This method will accept an adjacency matrix and return a hash map
def convertAdjMatrixToHashMap():
    # Create a hash map
    graph = defaultdict(list)

    # Create an adjacency matrix
    adjMatrix = [
        [1, 1, 0],
        [1, 1, 0],
        [0, 0, 1]
    ]

    # Loop through the adjacency matrix
    for i in range(len(adjMatrix)):
        for j in range(i + 1, len(adjMatrix)):
            # If the value is 1, add the edge to the hash map
            if adjMatrix[i][j] == 1:
                graph[i].append(j)
                graph[j].append(i)

    # Return the hash map
    return graph

if __name__ == "__main__":
    # Call the method
    graph = convertAdjMatrixToHashMap()

    # Print the hash map
    print(graph)
