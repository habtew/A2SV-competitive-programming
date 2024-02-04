class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        max_one = 0
        max_zero = 0
        ones_count = 0
        zeros_count = 0
        for num in s:
            if num == '1':
                ones_count += 1
                max_one = max(ones_count, max_one)
            else:
                ones_count = 0
        for num in s:
            if num == '0':
                zeros_count += 1
                max_zero = max(zeros_count, max_zero)
            else:
                zeros_count = 0
        return max_one > max_zero