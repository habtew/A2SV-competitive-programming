class Solution:
    def canJump(self, nums: List[int]) -> bool:
        x = 0
        n = len(nums)
        for i in range(n):
            if x < i:
                return False
            x = max(x, i + nums[i])
            
        return x >= n - 1