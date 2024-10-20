class Solution:
    def findGCD(self, nums: List[int]) -> int:
        mini = float('inf')
        maxi = -float('inf')
        for num in nums:
            mini = min(mini, num)
            maxi = max(maxi, num)
        num = 1
        for i in range(1, mini + 1):
            if mini % i == 0 and maxi % i == 0:
                num = max(num, i)

        return num