class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        directions = [(1, 2), (-1, 2), (1, -2), (-1, -2), (2, 1), (-2, 1), (2, -1), (-2, -1)]
    
        dp = [[[0] * n for _ in range(n)] for _ in range(k + 1)]
        dp[0][row][column] = 1.0
        
        for m in range(1, k + 1):
            for i in range(n):
                for j in range(n):
                    for d in directions:
                        prevI, prevJ = i - d[0], j - d[1]
                        if 0 <= prevI < n and 0 <= prevJ < n:
                            dp[m][i][j] += dp[m - 1][prevI][prevJ] / 8.0
        
        total_probability = 0
        for i in range(n):
            for j in range(n):
                total_probability += dp[k][i][j]
        
        return total_probability