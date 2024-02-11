class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = ''
        for c in s:
            if c.lower() in 'aeiou':
                vowels += c
        vowels = ''.join(sorted(vowels))
        result = ''
        for c in s:
            if c.lower() in 'aeiou':
                result += vowels[0]
                vowels = vowels[1:]
            else:
                result += c
        return result