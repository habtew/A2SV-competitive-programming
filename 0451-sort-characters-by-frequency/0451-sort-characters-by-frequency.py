class Solution:
    def frequencySort(self, s: str) -> str:
        dict_s = Counter(s)
        sorted_s = dict(sorted(dict_s.items(), key= lambda x: x[1], reverse=True))
        answer = ''
        for key, val in sorted_s.items():
            answer += key*val
        return answer