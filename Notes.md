#   Sorting

1. Bubble Sort - O(n^2)
2. Insertion Sort - O(n^2) --> Stable
3. Merge Sort - O(n^log(n)) --> Stable
4. Quick Sort - O(n^log(n)), Worst case is O(n^2)
5. Heap Sort - O(n^log(n))
6. Counting Sort - O(n)
7. Radix Sort - O(n)


#   Graph

-   The number of nodes in a graph is denoted by the letter V, and the number of edges by E.
-   Typically, E = |2V|
-   There are two types of graphs - directed graphs and undirected graphs. There are further two subcategories of graphs within each - cyclic and acyclic graphs. Literally, graphs with cycles and without cycles.

##  Traversing Graphs

-   There are two broad ways to traverse graphs - using BFS or DFS
-   BFS uses a queue to add all the neighbours of the current node. This algorithm is iterative
-   DFS uses a recursive function to go deep into the neighbours of a single node
-   The complexity of both is O(V+E)

##  Topological Sorting

-   This algorithm is an important algorithm. It is also called Khan's algorithm.
-   It can only be used on a DAG(directed acyclic graph) to find a relative ordering of the nodes
-   The complexity is O(V+E)
-   This algorithm can be used when finding shortest/longest path in a DAG or to find a relative order in a DAG
-   However, finding the shortest/longest path in a directed, cyclical graph is an NP-hard problem


#   Important algorithms to note

1. Kadane's Algorithm (to find maximum subarray sum)
2. Kahn's Algorithm (Graph topological sorting)