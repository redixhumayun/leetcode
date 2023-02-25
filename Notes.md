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
-   There are two types of graphs - directed graphs and undirected graphs. There are a further two subcategories of graphs within each - cyclic and acyclic graphs. Literally, graphs with cycles and without cycles.
-   Graphs can also be divided into weighted and unweighted graphs

##  Traversing Graphs

-   There are two broad ways to traverse graphs - using BFS or DFS.
-   The complexity of both is O(V+E)

### BFS
-   BFS uses a queue to add all the neighbours of the current node. This algorithm is iterative

### DFS
-   DFS uses a recursive function to go deep into the neighbours of a single node

##  Topological Sorting

-   This algorithm is an important algorithm. It is also called Khan's algorithm.
-   It can only be used on a DAG(directed acyclic graph) to find a relative ordering of the nodes
-   The complexity is O(V+E)
-   This algorithm can be used when finding shortest/longest path in a DAG or to find a relative order in a DAG
-   However, finding the shortest/longest path in a directed, cyclical graph is an NP-hard problem

## Disjoint Set Unions

These data structures combine nodes into separate sets, depending on whether they share the same root or not. This way it is easy to tell if two nodes belong to the same component, for instance. If two nodes have the same root node, then they belong to the same component.

These structures are useful when traversing an incoming set of edges, presented one at a time.

-   The main algorithms to note here are:
    -   Quick Find
    -   Quick Union
    -   Path Compression

Two main functions to think about:
    1. find()
    2. union()

Implementing `find()` in O(1) time will provide the Quick Find algorithm
Implementing `union()` in O(log(n)) time will provide the Quick Union algorithm
Path compression is an optimisation to improve the overall runtime of these algorithms.

![](/assets/img/Disjoint_Sets.png)

Optimised version of quick union runs in O(N) on average

##  Minimum Spanning Trees (MST)

### What is a spanning tree?

A spanning tree is a connected subgraph in an undirected graph where all vertices are connected with the minimum number of edges.

![](/assets/img/spanning-tree.png)

`[(A, B), (A, C), (A, D), (A, E)]` form a spanning tree.

### What is a minimum spanning tree?

A minimum spanning tree is a spanning tree with the minimum possible total edge weight in a “weighted undirected graph”.

![](/assets/img/mst.png)

`[(A, E), (A, B), (B, C), (C, D)]` forms one MST. One graph can have multiple MST's.

### What Is A Cut?

![](/assets/img/cut-property.png)

There are two subsets in this graph: `(B, A, E)` and `(C, D)`

## Algorithms For Graphs With Weighted Edges
1. Kruskal's Algorithm

    Uses a greedy strategy to construct a minimum spanning tree(MST). The list of edges is sorted by weight in ascending order and if including the current edge does not cause a cycle, then it is included. Uses Union Find data structure to construct the MST. Use priority queue to sort the list of edges by ascending weight

    ![](/assets/img/kruskal-algo.gif)

    Complexity: Sorting edges -> O(ElogE)
                Checking whether both ends of an edge belong to the same component using Quick Union -> O(V)
                Overall -> O(ElogE)
    Space Complexity: O(V) for the union-find data structure

    Look at [this problem](/graph/min-cost-to-connect-all-points-using-kruskal.py) for an implementation


2. Prim's Algorithm

    Uses a greedy strategy to find all outgoing edges from a node that go to nodes that are not yet part of the MST. Picks the minimum among these. Uses a priority queue to maintain the list of edges going out from one node according to their weights in ascending order.

    ![](/assets/img/prims-algo.gif)

    Complexity -> Sorting using binary heap -> O(ElogV)
    Space Complexity -> O(V)

    Look at [this problem](/graph/min-cost-to-connect-all-points-using-prim.py) for an implementation

#   Important algorithms to note

1. Kadane's Algorithm (to find maximum subarray sum)
2. Kahn's Algorithm (Graph topological sorting)
3. Quick Find, Quick Union and Path Compression for Disjoint Set data structures
4. Kruskal's and Prim's algorithm to construct MST