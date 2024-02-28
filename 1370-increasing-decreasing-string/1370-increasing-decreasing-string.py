class Solution:
    def sortString(self, s: str) -> str:
        char_count = [0] * 26
        for char in s:
            char_count[ord(char) - ord('a')] += 1
        
        result = []
        
        while any(char_count): 
            for i in range(26):
                if char_count[i] > 0:
                    result.append(chr(ord('a') + i))
                    char_count[i] -= 1
            
            for i in range(25, -1, -1):
                if char_count[i] > 0:
                    result.append(chr(ord('a') + i))
                    char_count[i] -= 1
        
        return ''.join(result)