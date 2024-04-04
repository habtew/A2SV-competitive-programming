class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        shift_pre = [0] * (len(s) + 1)
        
        for shift in shifts:
            if shift[2] == 0:
                shift_pre[shift[0]] += -1
                shift_pre[shift[1] + 1] += 1
            else:
                shift_pre[shift[0]] += 1
                shift_pre[shift[1] + 1] += -1
 
        pre = 0
        for i in range(len(shift_pre)):
            shift_pre[i] += pre
            pre = shift_pre[i]


        result = ''
        for i in range(len(s)):
            index = ord(s[i]) - ord('a')
            new_char = chr(((index + shift_pre[i]) % 26) + ord('a'))
            result += new_char
        
        return result
