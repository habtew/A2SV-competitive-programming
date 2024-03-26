class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        running_sum = [0]*len(nums)
        pre = 0
        for i in range(len(nums)):
            pre += nums[i]
            running_sum[i] = pre
        return running_sum