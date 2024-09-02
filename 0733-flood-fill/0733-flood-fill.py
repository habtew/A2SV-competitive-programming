class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color:
            return image
        
        n, m = len(image), len(image[0])
        prev = image[sr][sc]
        def dfs(x, y):
            if x < 0 or x >= n or y < 0 or y >= m or image[x][y] != prev:
                return
            image[x][y] = color
            dfs(x - 1, y)
            dfs(x + 1, y)
            dfs(x, y - 1)
            dfs(x, y + 1)
        dfs(sr, sc)
        return image