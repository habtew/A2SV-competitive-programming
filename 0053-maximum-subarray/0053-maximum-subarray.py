class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float('-inf')
        pre = 0
        
        for i in range(len(nums)):
            if pre < 0:
                pre = 0
            pre += nums[i]
            max_sum = max(pre, max_sum)
        
        return max_sum
    
        
    
        