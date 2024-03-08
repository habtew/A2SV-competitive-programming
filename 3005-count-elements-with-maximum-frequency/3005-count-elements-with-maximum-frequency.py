class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq = Counter(nums)
        larg = max([num for num in freq.values()])
        
        count = 0
        for val in freq.values():
            if val >= larg:
                count += val
        return count