class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        # result = [0] * 2 * n
        left1 = 0
        left2 = n
        result = []

        while left1 < n or left2 < 2*n:
            result.append(nums[left1])
            result.append(nums[left2])
            left1 += 1
            left2 += 1

        return result