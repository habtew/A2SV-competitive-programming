class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        arr = []
        
        for i in range(len(s)):
            left = i
            right = i
            while left >= 0 and s[left] != c:
                left -= 1
            while right < len(s) and s[right] != c:
                right += 1
                
            if s[i] == c:
                arr.append(0)
            else:
                if left < 0:
                    arr.append(right - i)
                elif right >= len(s):
                    arr.append(i - left)
                else:
                    arr.append(min(right - i, i - left))
                    
        return arr