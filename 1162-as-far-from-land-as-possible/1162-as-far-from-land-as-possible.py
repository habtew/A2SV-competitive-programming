class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        queue = deque()
        
        # Add all land cells to the queue
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    queue.append((i, j))

        max_d = -1
        len_qu = len(queue)

        # If there are no land cells or all cells are land cells, return -1
        if len_qu == 0 or len_qu == n * n:
            return -1
        
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        
        while queue:
            max_d += 1
            for _ in range(len(queue)):
                i, j = queue.popleft()
                for di, dj in directions:
                    x, y = i + di, j + dj
                    if 0 <= x < n and 0 <= y < n and grid[x][y] == 0:
                        grid[x][y] = 1
                        queue.append((x, y))
        
        return max_d