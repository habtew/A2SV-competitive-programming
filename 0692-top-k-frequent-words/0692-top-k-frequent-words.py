class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        words_count = Counter(words)
        sorted_word = sorted(words_count.items(), key= lambda x: (-x[1], x[0]))
        res = [word for word, _ in sorted_word[:k]]
        return res
        