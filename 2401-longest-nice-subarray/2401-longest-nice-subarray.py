class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        used = 0
        start = 0
        n = len(nums)
        result = 0

        for i in range(n):
            while used & nums[i] != 0:
                # reset used to 0
                used ^= nums[start]
                start += 1

            used |= nums[i]
            result = max(result, i - start + 1)
        
        return result