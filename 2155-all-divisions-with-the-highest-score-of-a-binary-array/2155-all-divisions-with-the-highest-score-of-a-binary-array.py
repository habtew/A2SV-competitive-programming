class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        n = len(nums)
        max_score = float('-inf')
        total_ones = sum(nums)
        current_ones_right = 0

        result = []

        for i in range(n + 1):
            zeros_left = i - current_ones_right
            ones_right = total_ones - current_ones_right

            score = zeros_left + ones_right

            if score > max_score:
                max_score = score
                result = [i]
            elif score == max_score:
                result.append(i)

            if i < n:
                current_ones_right += nums[i]

        return result