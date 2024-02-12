class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        counter = {}
        for num in nums:
            if num % 2 == 0 and num in counter:
                counter[num] += 1
            elif num % 2 == 0 and num not in counter:
                counter[num] = 1
        if not counter:
            return -1
        counter = (sorted(counter.items(), key=lambda x:(x[1], -x[0])))
        return counter[len(counter) - 1][0]
        