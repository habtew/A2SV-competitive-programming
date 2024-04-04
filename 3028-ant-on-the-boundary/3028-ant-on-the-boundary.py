class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        pre = 0
        count = 0
        for i in range(len(nums)):
            pre += nums[i]
            if pre == 0:
                count += 1
        return count