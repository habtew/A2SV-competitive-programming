class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)

        if total % 2 != 0:
            return False

        target = total // 2

        memo = {}
        
        def dp(i, curr_sum):
            if curr_sum == target:
                return True

            if i >= len(nums) or curr_sum > target:
                return False

            if (i, curr_sum) in memo:
                return memo[(i, curr_sum)]
             
            memo[(i, curr_sum)] = dp(i + 1, curr_sum + nums[i]) or dp(i + 1, curr_sum)
           
            return memo[(i, curr_sum)]

        return dp(0, 0)