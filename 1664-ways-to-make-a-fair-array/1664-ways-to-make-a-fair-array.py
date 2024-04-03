class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        prefix_sum = [[0, 0] for _ in range(len(nums) + 1)]
        for i in range(len(nums)):
            if i % 2 == 0:
                prefix_sum[i + 1][0] = prefix_sum[i][0] + nums[i]
                prefix_sum[i + 1][1] = prefix_sum[i][1]
            else:
                prefix_sum[i + 1][1] = prefix_sum[i][1] + nums[i]
                prefix_sum[i + 1][0] = prefix_sum[i][0]

        count = 0
        for i in range(len(nums)):
            if prefix_sum[i][0] + prefix_sum[-1][1] - prefix_sum[i + 1][1] == prefix_sum[i][1] + prefix_sum[-1][0] - prefix_sum[i + 1][0]:
                count += 1
        return count