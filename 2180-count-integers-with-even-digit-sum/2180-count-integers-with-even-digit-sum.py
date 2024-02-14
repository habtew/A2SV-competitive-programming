class Solution:
    def addDigit(self, num):
        result = 0
        while num:
            result += num % 10
            num //= 10
        return result
    def countEven(self, num: int) -> int:
        count = 0
        for i in range(1, num + 1):
            if self.addDigit(i) % 2 == 0:
                count += 1
        return count