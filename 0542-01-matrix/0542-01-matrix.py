class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])
        
        distance = [[-1] * cols for _ in range(rows)]
        
        queue = deque()
        
        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 0:
                    distance[i][j] = 0
                    queue.append((i, j))
        
        directions = ((-1, 0), (0, -1), (1, 0), (0, 1))
        
        while queue:
            i, j = queue.popleft()
            
            for di, dj in directions:
                x, y = i + di, j + dj
                if 0 <= x < rows and 0 <= y < cols and distance[x][y] == -1:
                    distance[x][y] = distance[i][j] + 1
                    queue.append((x, y))
        
        return distance