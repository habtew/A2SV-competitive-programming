class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos, neg = [], []
        for num in nums:
            if num > 0:
                pos.append(num)
            else:
                neg.append(num)
        result = [0] * len(nums)
        i = 0

        for j in range(len(pos)):
            result[i] = pos[j]
            result[i + 1] = neg[j]
            i += 2

        return result