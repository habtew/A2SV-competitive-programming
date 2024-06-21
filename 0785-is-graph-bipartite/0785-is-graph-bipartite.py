class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        color = [-1 for i in range(n)]
        
        def is_bipart(source):
            color[source]=0
            stack = [source]
            while stack:
                vertex = stack.pop()
                for i in graph[vertex]:
                    if color[vertex] == color[i]:
                        return False
                    if color[i] == -1:
                        stack.append(i)
                        color[i] = 1 - color[vertex]
            return True
        for i in range(n):
            if color[i] == -1 and not is_bipart(i):
                return False
        return True