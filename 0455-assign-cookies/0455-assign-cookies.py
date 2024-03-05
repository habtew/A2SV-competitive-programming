class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        count = 0
        index = 0
        while index < len(s) and count < len(g):
            if g[count] <= s[index]:
                count += 1
            index += 1
        return count