class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        nums_odd, nums_even = [], []
        for i in range(len(nums)):
            if i % 2 == 0:
                nums_even.append(nums[i])
            else:
                nums_odd.append(nums[i])
        nums_even.sort()
        nums_odd = sorted(nums_odd, reverse=True)
        res = [0] * len(nums)

        res[0::2] = nums_even
        res[1::2] = nums_odd
        return res
        