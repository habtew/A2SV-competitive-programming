class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        # [2,5,1, 3,4,7] 3 + 1, 4 + 1
        shuffled = []
        for i in range(n):
            shuffled.append(nums[i])
            shuffled.append(nums[n + i])
        return shuffled
