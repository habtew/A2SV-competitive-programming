class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        
        pre_sum = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                pre_sum[i][j] = (
                    mat[i - 1][j - 1] + 
                    pre_sum[i - 1][j] + 
                    pre_sum[i][j - 1] - 
                    pre_sum[i - 1][j - 1]
                )
        
        result = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                x1, y1 = max(i - k, 0), max(j - k, 0)
                x2, y2 = min(m - 1, i + k), min(n - 1, j + k)
                result[i][j] = (
                    pre_sum[x2 + 1][y2 + 1] - 
                    pre_sum[x1][y2 + 1] - 
                    pre_sum[x2 + 1][y1] + 
                    pre_sum[x1][y1]
                )
        
        return result