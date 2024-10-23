class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, val_diff: int) -> List[int]:
        min_idx = max_idx = 0
      
        for current_idx in range(indexDifference, len(nums)):
          
            compare_idx = current_idx - indexDifference
          
            if nums[compare_idx] < nums[min_idx]:
                min_idx = compare_idx
            if nums[compare_idx] > nums[max_idx]:
                max_idx = compare_idx
          
            if nums[current_idx] - nums[min_idx] >= val_diff:
                return [min_idx, current_idx]
          
            if nums[max_idx] - nums[current_idx] >= val_diff:
                return [max_idx, current_idx]
      
        return [-1, -1]