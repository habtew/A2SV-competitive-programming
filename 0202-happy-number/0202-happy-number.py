class Solution:
    def addDigits(self, n):
        result = 0
        while n:
            res = n % 10
            result += res * res
            n //= 10
        return result

    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = self.addDigits(n)

        return n == 1