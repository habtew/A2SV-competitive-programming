class Solution:
    def reverseWords(self, s: str) -> str:
        result = []
        for word in s.split():
            if word:
                result.append(word)
        result.reverse()
        return ' '.join(result)