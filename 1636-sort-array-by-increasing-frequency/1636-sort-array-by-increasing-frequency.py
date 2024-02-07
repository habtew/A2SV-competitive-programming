class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        nums_count = Counter(nums)
        sorted_nums_count = dict(sorted(nums_count.items(), key=lambda x: (x[1], -x[0])))
        result = [num for num, count in sorted_nums_count.items() for _ in range(count)]
        return result