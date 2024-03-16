class Solution:
    def reverse(self, num):
        rev = 0
        while num:
            rev = rev * 10 + num % 10
            num //= 10
        return rev

    def countDistinctIntegers(self, nums: List[int]) -> int:
        result = [num for num in nums]
        for num in nums:
            result.append(self.reverse(num))
        return len(set(result))
