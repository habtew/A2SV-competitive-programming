class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        num_ones = {}
        for num in arr:
            num_ones[num] = bin(num).count('1')
        sorted_nums = sorted(arr, key=lambda x: (num_ones[x], x))
        return sorted_nums