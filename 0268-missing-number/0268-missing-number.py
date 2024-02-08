class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total = sum(range(len(nums) + 1))
        total_arr = sum(nums)

        return total - total_arr