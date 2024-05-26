class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        pre = Counter({0: 1})
        total = 0
        odd_count = 0

        for num in nums:
            if num % 2 == 1:
                odd_count += 1
            if odd_count - k in pre:
                total += pre[odd_count - k]
            pre[odd_count] += 1
        
        return total