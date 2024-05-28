class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        l = 0
        n = len(s)
        max_length = 0
        sum_diff = 0
        for i in range(n):
            sum_diff += abs(ord(s[i]) - ord(t[i]))
            while sum_diff > maxCost:
                sum_diff -= abs(ord(s[l]) - ord(t[l]))
                l += 1
            max_length = max(max_length, i - l + 1)
        return max_length