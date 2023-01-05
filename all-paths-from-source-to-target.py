from typing import List

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        def dfs(node, curr):
            if node == len(graph) - 1:
                #   This is the n-1th node
                # ans.append(list(seen))
                ans.append(curr[:])
            for neighbour in graph[node]:
                if neighbour not in seen:
                    curr.append(neighbour)
                    seen.add(neighbour)
                    dfs(neighbour, curr)
                    seen.remove(neighbour)
                    curr.pop()

        ans = []
        seen = set()
        seen.add(0)
        dfs(0, [0])
        return ans

if __name__ == "__main__":
    s = Solution()
    print(s.allPathsSourceTarget([[1,2],[3],[3],[]]))
    print(s.allPathsSourceTarget([[4,3,1],[3,2,4],[3],[4],[]]))
    # print(s.allPathsSourceTarget([[1],[]]))
    # print(s.allPathsSourceTarget([[1,2,3],[2],[3],[]]))
    # print(s.allPathsSourceTarget([[1,3],[2],[3],[]]))