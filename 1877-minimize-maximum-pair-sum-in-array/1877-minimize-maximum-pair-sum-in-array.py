class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        larg = 0
        n = len(nums)
        for i in range(n // 2):
            if nums[i] + nums[n -i -1] > larg:
                larg = nums[i] + nums[n - i -1]
        return larg