class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # memo
        memo = {}
        n = len(nums)
        def dp(i, curr_sum):
            if i == n:
                return 1 if curr_sum == target else 0

            if (i, curr_sum) in memo:
                return memo[(i, curr_sum)]


            memo[(i, curr_sum)] = dp(i + 1, curr_sum + nums[i]) + dp(i + 1, curr_sum - nums[i])

            return memo[(i, curr_sum)]
        return dp(0, 0)