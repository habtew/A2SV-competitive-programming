class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        if n == 1:
            return '0'
        mid = pow(2, n - 1)
        if k == mid:
            return '1'
        if k < mid:
            return self.findKthBit(n - 1, k)
        return '1' if self.findKthBit(n - 1, mid * 2 - k) == '0' else '0'