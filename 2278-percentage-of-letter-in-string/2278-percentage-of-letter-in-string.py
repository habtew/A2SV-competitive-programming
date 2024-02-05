class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        count_letter = s.count(letter)
        return int((count_letter / len(s)) * 100)