class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        
        def rob_house(index: int) -> int:
            if index >= len(nums):
                return 0
            
            if index in memo:
                return memo[index]
            
            rob_current = nums[index] + rob_house(index + 2)
            
            skip_current = rob_house(index + 1)
            memo[index] = max(rob_current, skip_current)
            
            return memo[index]
        return rob_house(0)