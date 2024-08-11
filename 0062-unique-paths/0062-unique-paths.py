class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}
        def dp(i, j):
            if i == m - 1 and  j == n - 1:
                return 1
            if (i, j) in memo:
                return memo[(i, j)]
            move_right = 0
            if i + 1 < m:
                move_right = dp(i + 1, j)
            move_left = 0
            if j + 1 < n:
                move_left = dp(i, j + 1)

            memo[(i, j)] = move_right + move_left

            return memo[(i, j)]

        return dp(0, 0)