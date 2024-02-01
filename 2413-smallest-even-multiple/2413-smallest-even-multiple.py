class Solution:
    def gcd(self, a, b):
        if self.b == 0:
            return a
        return gcd(b, a % b)

    def smallestEvenMultiple(self, n: int) -> int:
        return int((n * 2) / gcd(n, 2))
        