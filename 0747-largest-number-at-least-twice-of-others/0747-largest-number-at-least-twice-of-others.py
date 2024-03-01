class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        largest, second_largest = float('-inf'), float('-inf')
        
        for num in nums:
            if num > largest:
                second_largest = largest
                largest = num
            elif num > second_largest and num != largest:
                second_largest = num
        if largest >= second_largest * 2:
            return nums.index(largest)
        return -1