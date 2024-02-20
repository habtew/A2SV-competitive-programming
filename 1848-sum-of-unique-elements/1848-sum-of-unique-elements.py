class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        freq = Counter(nums)
        result = sum([key for key, count in freq.items() if count <= 1])
        return result