class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        row, col = len(maze), len(maze[0])
        i, j = entrance
        
        queue = deque([(i, j)])
        
        maze[i][j] = '+'
        
        ans = 0
        directions = [[0, -1], [0, 1], [-1, 0], [1, 0]]
        while queue:
            ans += 1
            for _ in range(len(queue)):
                i, j = queue.popleft()
                for di, dj in directions:
                    x, y = i + di, j + dj
                    if 0 <= x < row and 0 <= y < col and maze[x][y] == '.':
                        if x == 0 or x == row - 1 or y == 0 or y == col - 1:
                            if [x, y] != entrance:
                                return ans
                        queue.append((x, y))
                        maze[x][y] = '+'
                    
        return -1