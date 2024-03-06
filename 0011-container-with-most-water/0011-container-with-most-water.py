class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        
        area = 0
        
        while left < right:
            if height[left] < height[right]:
                ar = height[left] * (right - left)
                area = max(area, ar)
                left += 1
            else:
                ar = height[right] * (right - left)
                area = max(area, ar)
                right -= 1
        return area