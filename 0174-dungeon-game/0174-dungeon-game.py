class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        n, m = len(dungeon), len(dungeon[0])
        memo = {}
        def dp(i, j):
            if i == n - 1 and j == m - 1:
                return max(1, 1 - dungeon[i][j])
            if i >= n or j >= m:
                return float('inf')
            if (i, j) in memo:
                return memo[(i, j)]
            min_health_on_exit = min(dp(i + 1, j), dp(i, j + 1))
            required_health = max(1, min_health_on_exit - dungeon[i][j])
            memo[(i, j)] = required_health
            return required_health
        
        return dp(0, 0)