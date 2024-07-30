class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        def dfs(index):
            if node_colors[index]:
                return node_colors[index] == 2
            
            node_colors[index] = 1
            
            for next_index in graph[index]:
                if not dfs(next_index):
                    return False
                
            node_colors[index] = 2
            return True
        n = len(graph)
        node_colors = [0] * n
        safe_nodes = [index for index in range(n) if dfs(index)]
        return safe_nodes