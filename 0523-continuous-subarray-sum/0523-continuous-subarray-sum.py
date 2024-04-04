class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        nums_rem = {0: -1}

        pre = 0
        for i in range(len(nums)):
            pre += nums[i]
            rem = pre % k
            if  rem not in nums_rem:
                nums_rem[rem] = i
            elif i - nums_rem[rem] >= 2:
                return True
                
        return False