class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        count = 0
        left = 0
        right = len(nums) - 1
        while left < right:
            res = nums[left] + nums[right]
            if res == k:
                count += 1
                left += 1
                right -= 1
            elif res > k:
                right -= 1
            else:
                left += 1
        
        return count