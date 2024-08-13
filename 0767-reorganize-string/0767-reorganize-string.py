class Solution:
    def reorganizeString(self, s: str) -> str:
        n = len(s)
        counted = Counter(s)
        max_freq = max(counted.values())
      
        if max_freq > (n + 1) // 2:
            return ''
      
        i = 0
      
        reorganized = [None] * n
      
        for char, freq in counted.most_common():
            while freq:
                reorganized[i] = char
                freq -= 1
                i += 2
                if i >= n:
                    i = 1
      
        return ''.join(reorganized)