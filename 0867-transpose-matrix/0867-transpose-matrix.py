class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        row = len(matrix[0])
        column = len(matrix)
        
        result = [[0 for _ in range(column)] for _ in range(row)]
        for i in range(row):
            for j in range(column):
                result[i][j] = matrix[j][i]
        
        return result