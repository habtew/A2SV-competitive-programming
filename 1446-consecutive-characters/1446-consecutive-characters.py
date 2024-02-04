class Solution:
    def maxPower(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            count  = 0
            for j in range(i, len(s)):
                if s[i] == s[j]:
                    count += 1
                else:
                    break
            res = max(res, count)
        return res