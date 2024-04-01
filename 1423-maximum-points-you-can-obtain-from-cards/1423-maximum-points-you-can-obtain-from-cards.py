class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        total = sum(cardPoints)
        window_size = n - k
        window_sum = sum(cardPoints[:window_size])
        answer = 0

        if window_size == 0:
            return total

        for i in range(n - window_size + 1):
            if i > 0:
                window_sum -= cardPoints[i - 1]
                window_sum += cardPoints[i + window_size - 1]
            answer = max(answer, total - window_sum)
        
        return answer