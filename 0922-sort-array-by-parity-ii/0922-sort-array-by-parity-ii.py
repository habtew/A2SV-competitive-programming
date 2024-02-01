class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        odd, even = [], []
        for num in nums:
            if num % 2 == 0:
                even.append(num)
            else:
                odd.append(num)
        result = [0]*len(nums)
        i = 0
        for j in range(len(odd)):
            result[i] = even[j]
            result[i + 1] = odd[j]
            i += 2
        return result