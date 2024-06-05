class Solution:
    def longestPalindrome(self, s: str) -> int:
        dict_s = Counter(s)
        count = 0
        one = False
        for val in dict_s.values():
            count += (val // 2) * 2

            if val % 2 == 1:
                one = True
        if one:
            count += 1
        return count