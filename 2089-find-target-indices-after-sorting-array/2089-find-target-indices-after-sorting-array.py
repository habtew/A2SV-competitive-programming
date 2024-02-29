class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        if target not in nums:
            return []
        result = []
        nums.sort()
        for i in range(len(nums)):
            if target == nums[i]:
                result.append(i)
        return result