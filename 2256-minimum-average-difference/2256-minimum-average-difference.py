class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        n = len(nums)
        pre = [0] * n
        suf = [0] * n
        
        pre[0] = nums[0]
        for i in range(1, n):
            pre[i] = pre[i - 1] + nums[i]
        
        suf[n - 1] = nums[-1]
        for i in range(n - 2, -1, -1):
            suf[i] = suf[i + 1] + nums[i]

        min_diff = float('inf')
        min_index = -1

        for i in range(n):
            left_avg = pre[i] // (i + 1)
            right_avg = suf[i + 1] // (n - i - 1) if i != n - 1 else 0
            avg_diff = abs(left_avg - right_avg)

            if avg_diff < min_diff:
                min_diff = avg_diff
                min_index = i

        return min_index