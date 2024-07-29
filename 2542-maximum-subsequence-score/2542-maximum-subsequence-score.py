class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        combined = []
        for i in range(len(nums1)):
            combined.append((nums2[i], nums1[i]))
        
        combined.sort(reverse=True)
        
        result = 0
        heap = []
        sum_heap = 0
        
        for num2, num1 in combined:
            heapq.heappush(heap, num1)
            sum_heap += num1
            
            if len(heap) > k:
                sum_heap -= heapq.heappop(heap)

            if len(heap) == k:
                result = max(result, sum_heap * num2)
        
        return result