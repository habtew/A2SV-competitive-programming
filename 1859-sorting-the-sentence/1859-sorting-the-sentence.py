class Solution:
    def sortSentence(self, s: str) -> str:
        words = {}
        for word in s.split():
            words[int(word[-1])] = word[:len(word) - 1]
        sorted_words = dict(sorted(words.items(), key = lambda x:x[0]))
        result = [val for val in sorted_words.values()]
        print(result)
        
        return ' '.join(result)