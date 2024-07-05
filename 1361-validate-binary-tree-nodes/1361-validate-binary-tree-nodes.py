class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        def find_root(x: int) -> int:
            if parents[x] != x:
                parents[x] = find_root(parents[x])
            return parents[x]

        parents = list(range(n))

        visited = [False] * n

        for i, (leftChild, rightChild) in enumerate(zip(leftChild, rightChild)):
            for child in (leftChild, rightChild):
                if child != -1:
                    if visited[child] or find_root(i) == find_root(child):
                        return False
                    
                    parents[find_root(i)] = find_root(child)
                    visited[child] = True
                    n -= 1

        return n == 1