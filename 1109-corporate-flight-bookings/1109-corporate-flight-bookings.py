class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        pre_sum = [0] * (n + 1)
        for book in bookings:
            pre_sum[book[0] - 1] += book[2]
            pre_sum[book[1]] -= book[2]
        
        pre = 0
        for i in range(len(pre_sum)):
            pre_sum[i] += pre
            pre = pre_sum[i]
        return pre_sum[:-1]