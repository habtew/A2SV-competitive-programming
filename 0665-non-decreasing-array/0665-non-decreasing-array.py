class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        # 1,2,3
        count = 0
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                if i > 0 and nums[i - 1] > nums[i + 1]:
                    nums[i + 1] = nums[i]
                count += 1
            else:
                continue
        if count <= 1:
            return True
        else:
            return False