class Solution:
    def getLucky(self, s: str, k: int) -> int:
        nums = ''
        for c in s:
            nums += str(ord(c) - 96)
        num = int(nums)
        for i in range(k):
            res = 0
            while num:
                res += num % 10
                num //= 10
            num = res
        return num