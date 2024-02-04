class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_power = 0
        current_power = 0
        for num in nums:
            if num == 1:
                current_power += 1
                max_power = max(current_power, max_power)
            else:
                current_power = 0
        return max_power