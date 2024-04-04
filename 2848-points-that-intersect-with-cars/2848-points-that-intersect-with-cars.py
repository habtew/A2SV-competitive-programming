class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        pre_cars = [0] * 102
        min_num = float('inf')
        max_num = float('-inf')
        for num in nums:
            min_num = min(min_num, min(num))
            max_num = max(max_num, max(num))
            pre_cars[num[0]] += 1
            pre_cars[num[1] + 1] -= 1
        
        pre = 0
        for i in range(len(pre_cars)):
            pre_cars[i] += pre
            pre = pre_cars[i]
        count = 0
        for i in range(len(pre_cars)):
            if pre_cars[i] >= 1:
                count += 1
        return count