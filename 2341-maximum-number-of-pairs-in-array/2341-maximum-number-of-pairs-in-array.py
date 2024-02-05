class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        nums_counter = Counter(nums)
        odd = 0
        even = 0
        for val in nums_counter.values():
            even += val
            if val % 2 == 1:
                odd += 1
            else:
                continue
        return [int((even - odd) / 2), odd]