class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        freq = {}
        for i in range(len(nums[0])):
            for num in nums:
                n = nums[0][i]
                if n in num and n in freq:
                    freq[n] += 1
                elif n in num and n not in freq:
                    freq[n] = 1
        return sorted([key for key, val in freq.items() if val == len(nums)])