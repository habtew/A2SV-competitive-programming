class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        nums = []
        for num in s.split():
            if num.isdigit():
                nums.append(int(num))
        left = 0
        right = 1
        while right < len(nums):
            if nums[left] >= nums[right]:
                return False
            left += 1
            right += 1
        return True