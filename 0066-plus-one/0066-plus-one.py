class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digit = 0
        i = 0
        while i < len(digits):
            digit = digit*10 + digits[i]
            i += 1
        digit += 1
        li = []
        while digit:
            li.insert(0, digit%10)
            digit //= 10
        return li