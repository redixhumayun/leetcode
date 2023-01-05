from collections import defaultdict

class Solution:
    def calcEquation(self, equations, values, queries):
        #   Build graph with weighted edges from the provided equations and values
        #   Build set indicating direct relationship between nodes. Indicate relationship 2-way
        graph = defaultdict(list)
        relations = set()
        for i in range(len(equations)):
            [from_node, to_node] = equations[i]
            weight = values[i]
            graph[from_node].append((to_node, weight))
            graph[to_node].append((from_node, 1/weight))
            relations.add((from_node, from_node))
            relations.add((to_node, to_node))
            relations.add((from_node, to_node))
            relations.add((to_node, from_node))

        results = [-1] * len(queries)
        for i in range(len(queries)):
            [num, den] = queries[i]
            neighbours = graph[num]
            neighbours_of_denominator = graph[den]
            if (num, den) in relations:
                if num == den:
                    results[i] = 1
                #   Pair has a direction relationship
                for neighbour in graph[num]:
                    (node, weight) = neighbour
                    if node == den:
                        results[i] = weight
            else:
                #   No direct relationship
                #   Check if these nodes exist in the graph
                if neighbours and neighbours_of_denominator and len(neighbours) == 1 and len(neighbours_of_denominator) == 1:
                    #   Check that only one equation is possible
                    (node1, weight1) = neighbours[0]
                    (node2, weight2) = neighbours_of_denominator[0]
                    results[i] = weight1 / weight2
        return results

if __name__ == '__main__':
    equations = [["a","e"],["b","e"]]
    values = [4.0,3.0]
    queries = [["a","b"],["e","e"],["x","x"]]
    print(Solution().calcEquation(equations, values, queries))