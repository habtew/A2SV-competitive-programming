class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, col = len(matrix), len(matrix[0])

        for i in range(row*col):
            r = i // col
            c = i % col

            if matrix[r][c] == target:
                return True
        return False