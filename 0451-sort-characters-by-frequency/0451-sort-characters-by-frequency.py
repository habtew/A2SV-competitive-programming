class Solution:
    def frequencySort(self, s: str) -> str:
        dict_s = Counter(s)
        sorted_dict = dict(sorted(dict_s.items(), key=lambda x: x[1], reverse=True))
        answer = ''
        for key, val in sorted_dict.items():
            answer += key*val
        return answer