class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res = []
        target = len(graph) - 1

        def dfs(node, curr):
            if node == target:
                res.append(curr.copy())
                return
            for val in graph[node]:
                curr.append(val)
                dfs(val, curr)
                curr.pop()
        dfs(0, [0])

        return res