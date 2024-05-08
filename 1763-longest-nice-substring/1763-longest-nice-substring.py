class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        
        def rec(s):
            if len(s) == 1 or len(s) == 0:
                return ''
            set_s = set(s)
            for i in range(len(s)):
                if not (s[i].lower() in set_s and s[i].upper() in set_s):
                    left, right = rec(s[:i]), rec(s[i + 1:])
                    if len(left) >= len(right):
                        return left
                    return right
            return s
        return rec(s)