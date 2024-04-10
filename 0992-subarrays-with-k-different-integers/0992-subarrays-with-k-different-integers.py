class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        num_freq = defaultdict(int)
        count = 0
        left = 0
        left_boundary = 0
        
        for right in range(len(nums)):
            num_freq[nums[right]] += 1
            while len(num_freq) > k:
                num_freq[nums[left]] -= 1
                
                if num_freq[nums[left]] == 0:
                    num_freq.pop(nums[left])
                left += 1
                left_boundary = left
                
            while num_freq[nums[left]] > 1:
                num_freq[nums[left]] -= 1
                left += 1
                
            if len(num_freq) == k:
                count += left - left_boundary + 1
        
        return count