class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        prev = nums[0]
        count = 0
        for i in range(1, n):
            if prev != nums[i]:
                count += n - i
                prev = nums[i]
        return count