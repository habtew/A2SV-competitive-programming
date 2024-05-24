class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix) - 1
        
        # row = 0
        
        while left < right:
            mid = (left + right ) // 2
            last = len(matrix[mid]) - 1
            
            if matrix[mid][last] < target:
                left = mid + 1
            else:
                right = mid
            
        left_sec = 0
        right_sec = len(matrix[left]) - 1
        while left_sec <= right_sec:
            mid = (left_sec + right_sec + 1) // 2

            if matrix[left][mid] == target:
                return True
            elif matrix[left][mid] < target:
                left_sec = mid + 1
            else:
                right_sec = mid - 1

        return False