class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        pre_sum = 0
        max_sum = float('-inf')

        for num in nums:
            if pre_sum < 0:
                pre_sum = 0
            pre_sum += num
            max_sum = max(max_sum, pre_sum)
        return max_sum