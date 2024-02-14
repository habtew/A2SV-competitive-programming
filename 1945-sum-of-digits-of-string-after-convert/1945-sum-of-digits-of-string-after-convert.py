class Solution:
    def addNum(self, num):
        result = 0
        while num > 0:
            result += num % 10
            num //= 10
        return result
    def getLucky(self, s: str, k: int) -> int:
        num = ''
        for c in s:
            num += str(ord(c) - 96)
        num = int(num)
        while k > 0:
            num = self.addNum(num)
            k -= 1
        return num