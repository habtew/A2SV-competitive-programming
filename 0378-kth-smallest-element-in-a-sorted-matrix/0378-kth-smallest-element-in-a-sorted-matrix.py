class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        row = len(matrix)
        col = len(matrix)
        arr = []
        for i in range(row * col):
            r = i // col
            c = i % col
            arr.append(matrix[r][c])
        arr.sort()
        return arr[k - 1]