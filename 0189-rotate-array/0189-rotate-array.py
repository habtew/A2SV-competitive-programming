class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k == 0:
            return nums
        if k > len(nums):
            k = k % len(nums)

        while k > 0:
            first = nums.pop()
            nums.insert(0, first)
            k -= 1
        return nums