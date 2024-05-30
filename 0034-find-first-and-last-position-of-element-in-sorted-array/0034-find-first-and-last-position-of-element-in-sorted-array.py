class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        if left >= len(nums) or nums[left] != target:
            return [-1, -1]

        start = left
        right = len(nums) - 1
        while start <= right:
            mid = (start + right) // 2
            if nums[mid] > target:
                right = mid - 1
            else:
                start = mid + 1
        
        return [left, right]