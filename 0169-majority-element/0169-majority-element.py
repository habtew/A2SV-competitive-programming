class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums_counted = Counter(nums)
        largest = 0
        n = int(len(nums) / 2)
        for key, val in nums_counted.items():
            if val > n:
                largest = key
        return largest
