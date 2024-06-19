class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        
        def dfs(r, c):
            if (r, c) in visited:
                return 0
            visited.add((r, c))
            perimeter = 0
            
            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if nr < 0 or nr >= rows or nc < 0 or nc >= cols or grid[nr][nc] == 0:
                    perimeter += 1
                else:
                    perimeter += dfs(nr, nc)
            
            return perimeter
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return dfs(r, c)
        
        return 0