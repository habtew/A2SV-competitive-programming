class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        
        l = 0
        f_count = 0
        t_max = 0

        for r in range(len(answerKey)):
            if answerKey[r] == 'F':
                f_count += 1
            while f_count > k:
                if answerKey[l] == 'F':
                    f_count -= 1
                l += 1
            t_max = max(t_max, r - l + 1)

        l = 0
        t_count = 0
        f_max = 0

        for r in range(len(answerKey)):
            if answerKey[r] == 'T':
                t_count += 1
            while t_count > k:
                if answerKey[l] == 'T':
                    t_count -= 1
                l += 1
            f_max = max(f_max, r - l + 1)
        return max(t_max, f_max)
