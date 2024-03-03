class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[0])
        result = 0
        
        for i in range(len(points) - 1):
            diff = points[i + 1][0] - points[i][0]
            if diff > result:
                result = diff
        
        return result