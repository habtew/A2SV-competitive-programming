class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        if target not in nums:
            return []
        result = []
        nums.sort()
        first = nums.index(target)
        while nums[first] == target:
            result.append(first)
            first += 1
            if first == len(nums):
                break
        return result