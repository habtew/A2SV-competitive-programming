class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0
        non_zero_index = 0
        result = []
        for num in nums:
            if num != 0:
                result.append(num)
            else:
                non_zero_index += 1
        return result + [0] * non_zero_index