class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        counter = {}
        for num in nums:
            if num in counter:
                return num
            else:
                counter[num] = 1
    