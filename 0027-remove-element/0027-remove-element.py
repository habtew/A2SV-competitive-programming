class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0  # Read pointer
        j = 0  # Write pointer

        while i < len(nums):
            if nums[i] != val:
                nums[j] = nums[i]
                j += 1
            i += 1

        return j