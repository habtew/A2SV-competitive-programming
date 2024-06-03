class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # -4, -1, -1, 0, 1, 2
        # 1, -1, 2
        nums.sort()
        result = []

        for i in range(len(nums) - 1):
            left = i + 1
            right = len(nums) - 1
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            target = -nums[i]

            while left < right:
                current_sum = nums[left] + nums[right]

                if target == current_sum:
                    result.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1

                elif current_sum < target:
                    left += 1
                else:
                    right -= 1
        return result
