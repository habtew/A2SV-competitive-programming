class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        common_word = []
        first_word = words[0]
        
        for char in set(first_word):
            count = first_word.count(char)
            for word in words[1:]:
                count = min(count, word.count(char))
            
            common_word.extend([char] * count)

        return common_word