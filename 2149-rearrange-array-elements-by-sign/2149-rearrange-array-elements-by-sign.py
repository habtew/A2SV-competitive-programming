class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)
        ptr1, ptr2 = 0, 1
        for num in nums:
            if num > 0:
                result[ptr1] = num
                ptr1 += 2
            else:
                result[ptr2] = num
                ptr2 += 2
        return result