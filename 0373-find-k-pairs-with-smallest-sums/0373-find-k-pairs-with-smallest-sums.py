class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        priority_queue = [[u + nums2[0], i, 0] for i, u in enumerate(nums1[:k])]
        heapify(priority_queue)

        result = []
        
                
        while priority_queue and k > 0:
            sum_pair, index1, index2 = heappop(priority_queue)
          
            result.append([nums1[index1], nums2[index2]])
          
            k -= 1
            if index2 + 1 < len(nums2):
                heappush(priority_queue, [nums1[index1] + nums2[index2 + 1], index1, index2 + 1])

        return result