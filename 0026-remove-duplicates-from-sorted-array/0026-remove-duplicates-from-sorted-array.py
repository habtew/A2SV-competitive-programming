class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 0
        right = 1
        count = 0
        n = len(nums) - 1
        while right <= len(nums) - 1:
            if nums[left] == nums[right]:
                nums.pop(right)
            else:
                left = right
                right += 1
        return len(nums)
            