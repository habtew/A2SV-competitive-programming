class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        arr = [float('-inf')] + arr + [float('-inf')]
        stack = []
        result = 0
        for i, num in enumerate(arr):
            while stack and arr[stack[-1]] > num:
                j = stack.pop()
                result += arr[j] * (i - j) * (j - stack[-1])
            stack.append(i)
        return result % (10**9 + 7)