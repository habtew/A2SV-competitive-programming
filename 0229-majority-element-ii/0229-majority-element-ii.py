class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        nums_count = Counter(nums)
        n = len(nums)
        occur = n // 3
        result = []
        for key, val in nums_count.items():
            if val > occur:
                result.append(key)
        return result