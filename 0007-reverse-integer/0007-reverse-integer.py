class Solution:
    def reverse(self, x: int) -> int:
        MAX = 2**31 - 1
        MIN = -2**31
        sign  = 1
        rev = 0
        if x < 0:
            sign = -1
            x = -1 * x
        while x:
            l = x % 10
            rev = rev * 10 + l
            x //= 10
        rev *= sign
        if rev > MAX or rev <  MIN:
            return 0
        else:
            return rev