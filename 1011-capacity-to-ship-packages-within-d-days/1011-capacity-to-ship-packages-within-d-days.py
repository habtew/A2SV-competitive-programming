class Solution:
    def findDays(self, weights, cap):
        days = 1
        load_weight = 0
        for i in range(len(weights)):
            if weights[i] + load_weight > cap:
                days += 1
                load_weight = weights[i]
            else:
                load_weight += weights[i]
        return days
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low = max(weights)
        high = sum(weights)
        while low <= high:
            mid = (low + high) // 2
            numDays = self.findDays(weights, mid)
            if numDays <= days:
                high = mid - 1
            else:
                low = mid + 1
        return low