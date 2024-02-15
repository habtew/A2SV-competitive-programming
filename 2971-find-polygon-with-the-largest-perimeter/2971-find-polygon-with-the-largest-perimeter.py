class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        for i in range(len(nums) - 2):
            if nums[i] < sum(nums[i + 1: ]):
                return (nums[i] + sum(nums[i + 1:]))
            
        return -1