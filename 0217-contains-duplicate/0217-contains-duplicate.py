class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dupl = {}
        for num in nums:
            if num in dupl:
                dupl[num] += 1
            else:
                dupl[num] = 1
        for val in dupl.values():
            if val > 1:
                return True
        return False
        