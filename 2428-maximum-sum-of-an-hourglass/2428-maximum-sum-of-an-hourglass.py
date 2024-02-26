class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        R = len(grid)
        C = len(grid[0])
        best = 0

        for x in range(1, R - 1):
            for y in range(1, C - 1):
                total = 0
                for dx in range(-1, 2):
                    for dy in range(-1, 2):
                        total += grid[x + dx][y + dy]
                total -= grid[x][y - 1]
                total -= grid[x][y + 1]
                best = max(best, total)

        return best