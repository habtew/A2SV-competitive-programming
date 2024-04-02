class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        m = len(grid[0])
        flattened_list = list(chain.from_iterable(grid))
        pre_prod = []
        pre = 1
        for i in range(len(flattened_list)):
            pre_prod.append(pre)
            pre = (pre *flattened_list[i]) % 12345
        suf = 1
        for i in range(len(flattened_list) - 1, -1, -1):
            pre_prod[i] *= suf % 12345
            suf = (suf * flattened_list[i]) % 12345
        
        matrix = [[pre_prod[i * m + j] % 12345 for j in range(m)] for i in range(n)]
        
        return matrix
        
        
        # n = len(grid)
        # m = len(grid[0])
        # pre_grid = [[0] * m for _ in range(n)]
        # pre = 1
        # for i in range(n):
        #     for j in range(m):
        #         pre_grid[i][j] = pre
        #         pre *= grid[i][j]
        # suf = 1
        # for i in range(n - 1, -1, -1):
        #     for j in range(m - 1, -1, -1):
        #         pre_grid[i][j] *= suf
        #         suf *= grid[i][j]
        # for i in range(n):
        #     for j in range(m):
        #         pre_grid[i][j] %= 12345
        # return pre_grid