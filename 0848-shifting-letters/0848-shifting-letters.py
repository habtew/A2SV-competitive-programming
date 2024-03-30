class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        shifts_suffix_sum = [0] * len(shifts)
        suff = 0
        answer = ''
        
        for i in range(len(shifts) - 1, -1, -1):
            suff = (suff + shifts[i]) % 26
            shifts_suffix_sum[i] = suff
        
        for i in range(len(shifts_suffix_sum)):
            val = ord(s[i]) - ord('a')
            val = (val + shifts_suffix_sum[i]) % 26
            answer += chr(ord('a') + val)
        
        return answer