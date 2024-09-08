class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        indegree = [0] * n
        for edge in edges:
            indegree[edge[1]] += 1
        count = 0
        for num in indegree:
            if num == 0:
                count += 1
        if count == 1:
            return indegree.index(0)
        return -1