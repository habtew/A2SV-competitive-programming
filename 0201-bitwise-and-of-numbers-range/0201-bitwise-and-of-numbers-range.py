class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        b = 0
        while left < right:
            left >>= 1
            right >>= 1
            b += 1
        return left << b