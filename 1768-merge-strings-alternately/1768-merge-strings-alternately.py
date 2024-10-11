class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        a, b = 0, 0
        new_str = ''
        while a < len(word1) and b < len(word2):
            new_str += word1[a]
            new_str += word2[b]
            a += 1
            b += 1
        new_str += word1[a:]
        new_str += word2[b:]
        return new_str