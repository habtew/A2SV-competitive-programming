class Solution:
    def findMinSpeed(self, piles, k):
        hours = 0
        for pile in piles:
            hours += (pile + k - 1) // k
        return hours
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)

        while low <= high:
            mid = (low + high) // 2
            hours = self.findMinSpeed(piles, mid)
            if hours <= h:
                high = mid - 1
            else:
                low = mid + 1
        return low
