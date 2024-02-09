class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # [2,2,,64,4,6] == 6 elements
        # 6/ 3 = 2 , element more than twice [2, 4, 6]
        nums_count = Counter(nums)
        n = len(nums)
        occur = n // 3
        result = []
        for key, val in nums_count.items():
            if val > occur:
                result.append(key)
        return result