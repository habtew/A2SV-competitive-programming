class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        nums_even, nums_odd = [], []
        for num in nums:
            if num % 2 == 0:
                nums_even.append(num)
            else:
                nums_odd.append(num)
        return[*nums_even, *nums_odd]