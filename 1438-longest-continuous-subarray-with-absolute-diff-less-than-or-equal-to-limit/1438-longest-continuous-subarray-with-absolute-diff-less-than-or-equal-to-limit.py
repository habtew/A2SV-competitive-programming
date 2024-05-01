class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        maxq, minq = deque(), deque()
        start = 0
        max_length = 0
        
        for end in range(len(nums)):
            while maxq and nums[maxq[-1]] <= nums[end]:
                maxq.pop()
            maxq.append(end)
            
            while minq and nums[minq[-1]] >= nums[end]:
                minq.pop()
            minq.append(end)
            
            while nums[maxq[0]] - nums[minq[0]] > limit:
                start += 1
                if maxq[0] < start:
                    maxq.popleft()
                if minq[0] < start:
                    minq.popleft()
            
            max_length = max(max_length, end - start + 1)
        
        return max_length