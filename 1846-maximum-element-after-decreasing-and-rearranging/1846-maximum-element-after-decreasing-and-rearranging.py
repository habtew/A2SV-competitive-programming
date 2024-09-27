class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, nums: List[int]) -> int:
        nums.sort()
        nums[0] = 1
        for i in range(1, len(nums)):
            if abs(nums[i] - nums[i - 1]) > 1:
                nums[i] = nums[i - 1] + 1

        return nums[-1]