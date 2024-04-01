class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        pre_capacity = [0] * 1001

        for trip in trips:
            pre_capacity[trip[1]] += trip[0]
            pre_capacity[trip[2]] -= trip[0]
        total_ind = max(pre_capacity)
        total = 0
        for i in range(1, len(pre_capacity)):
            pre_capacity[i] += pre_capacity[i - 1]
            total = max(total, pre_capacity[i])
        total = max(total_ind, total)
        return total <= capacity