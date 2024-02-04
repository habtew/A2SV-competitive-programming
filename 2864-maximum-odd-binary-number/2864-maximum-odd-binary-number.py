class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        s = sorted(s, reverse=True)
        return ''.join(s[1:] + ['1'])